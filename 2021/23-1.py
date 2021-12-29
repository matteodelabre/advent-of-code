from itertools import product
from heapq import heappush, heappop
from math import inf

# Room layout (usable cells are alnum)
layout = """\
#############
#01.2.3.4.56#
###7#9#B#D###
  #8#A#C#E#
  #########
""".splitlines()

hallway = layout[1][layout[1].find("#") + 1 : layout[1].rfind("#")]
rooms = {"A": "78", "B": "9A", "C": "BC", "D": "DE"}
room_size = len(rooms["A"])

# Compute the distances between any two cells, assuming no obstacles
distances = {}

for sy in range(len(layout)):
    for sx in range(len(layout[sy])):
        cell = layout[sy][sx]
        if not cell.isalnum(): continue

        visited = {(sx, sy): 0}
        stack = [(sx, sy, 0)]

        while stack:
            cx, cy, dist = stack.pop()

            for nx, ny in ((cx - 1, cy), (cx + 1, cy),
                    (cx, cy - 1), (cx, cy + 1)):
                if (nx, ny) not in visited and layout[ny][nx] != "#":
                    visited[(nx, ny)] = dist
                    stack.append((nx, ny, dist + 1))

        distances[cell] = {
            layout[cy][cx]: dist
            for (cx, cy), dist in visited.items()
            if layout[cy][cx].isalnum()
        }

# Get the amphipod kind for the given position in a configuration
def kind_of(position):
    return chr(ord("A") + position // room_size)

# Get the unit cost of moving an amphipod of the kind matching a position
def cost_of(position):
    return 10 ** (position // room_size)

# Check if position in hallway is to the left of given room kind
def is_left_of(kind, query):
    return query in "".join(hallway.split(".")[: ord(kind) - ord("A") + 1])

# Check if a configuration is terminal
def is_goal(config):
    return all(
        set(cells) == set(
            position[0] for position in
            config[room_size * i : room_size * (i + 1)]
        )
        for i, (room, cells) in enumerate(sorted(rooms.items()))
    )

# Find the configurations reachable by moving a given position
# from a starting configuration
def find_reachable(config, position):
    origin, moved = config[position]
    kind = kind_of(position)

    # Only allow moving positions that haven’t already moved out of a room
    # or are still in the hallway
    if config[position][0] not in hallway and config[position][1]:
        return {}, False

    # Disallow moving out positions that are already in the right place
    if config[position][0] in rooms[kind] and all(
            kind_of(oth_pos) == kind
            for oth_pos in range(len(config))
            if config[oth_pos][0] in rooms[kind]
            and config[oth_pos][0] > config[position][0]):
        return {}, False

    sy = min(y for y, row in enumerate(layout) if row.find(origin) != -1)
    sx = layout[sy].find(origin)

    visited = {}
    stack = [(sx, sy, 0)]

    while stack:
        cx, cy, ce = stack.pop()
        visited[(cx, cy)] = ce

        for nx, ny in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)):
            if (nx, ny) in visited: continue

            # Cannot move to or through already occupied locations, or walls
            if layout[ny][nx] == "#": continue
            if any(state[0] == layout[ny][nx] for state in config): continue

            stack.append((nx, ny, ce + 1))

    closing_move = None

    for cx, cy in list(visited.keys()):
        if (cx, cy) == (sx, sy):
            # Disallow null moves
            del visited[(cx, cy)]
        elif not layout[cy][cx].isalnum():
            # Disallow moving to temporary positions or walls
            del visited[(cx, cy)]
        elif layout[cy][cx] not in hallway:
            if layout[cy][cx] not in rooms[kind]:
                # Only allow moving to rooms of correct kind
                del visited[(cx, cy)]
            else:
                for other_position, (other_origin, _) in enumerate(config):
                    other_kind = kind_of(other_position)
                    if kind != other_kind and other_origin in rooms[kind]:
                        # Disallow moving to a room shared with other kinds
                        del visited[(cx, cy)]
                        break
                else:
                    # Always move to the deepest available position in a room
                    if (cy + 1, cx) in visited:
                        printy = True
                        del visited[(cx, cy)]
                    else:
                        closing_move = (cx, cy)
        elif origin in hallway:
            # Disallow moving to other locations inside the hallway
            del visited[(cx, cy)]

    if closing_move:
        return {
            layout[closing_move[1]][closing_move[0]]: visited[closing_move]
        }, True
    else:
        return {
            layout[cy][cx]: ce
            for (cx, cy), ce in visited.items()
        }, False

# Get a lower bound on the energy needed to advance a configuration
# towards a goal configuration
def estimate_energy(config):
    total = 0

    # Crossing configurations can never reach the goal
    for pos1, pos2 in product(range(len(config)), repeat=2):
        kind1 = kind_of(pos1)
        cell1 = config[pos1][0]

        kind2 = kind_of(pos2)
        cell2 = config[pos2][0]

        if cell1 < cell2 and \
                kind1 > kind2 and \
                cell1 in hallway and cell2 in hallway and \
                is_left_of(kind1, cell1) and \
                is_left_of(kind1, cell2) and \
                not is_left_of(kind2, cell1) and \
                not is_left_of(kind2, cell2):
            return inf

    for pos in range(len(config)):
        kind = kind_of(pos)
        unit = cost_of(pos)

        total += unit * min(
            distances[config[pos][0]][target]
            for target in rooms[kind]
        )

    return total

# Update a position in a configuration
def update_config(config, position, coord, dist):
    next_config = (
        config[:position]
        + ((coord, True),)
        + config[position+1:]
    )
    energy_delta = dist * cost_of(position)
    return next_config, energy_delta

# Find the energy required to reach any other configuration
def explore(start):
    energies = {start: 0}
    opened = {start: 0}
    closed = set()
    queue = [(0, start)]

    while queue:
        _, config = heappop(queue)
        energy = energies[config]

        if config in closed:
            continue

        del opened[config]
        closed.add(config)

        if is_goal(config):
            return energy

        for position in range(len(config)):
            moves, has_closing_move = find_reachable(config, position)

            for coord, dist in moves.items():
                next_config, energy_delta = update_config(
                    config, position, coord, dist
                )
                total = energy + energy_delta

                if total == inf:
                    continue

                if next_config not in energies or total < energies[next_config]:
                    priority = total + estimate_energy(next_config)

                    if next_config not in closed and (next_config not in opened \
                            or opened[next_config] > priority):
                        energies[next_config] = total
                        opened[next_config] = priority
                        heappush(queue, (priority, next_config))

            if has_closing_move:
                break

    return None

# Read starting configuration
start = [None] * sum(len(room) for room in rooms.values())

for layout_row in layout:
    start_row = input()
    for layout_cell, start_cell in zip(layout_row, start_row):
        if start_cell in rooms:
            position = (ord(start_cell) - ord("A")) * room_size
            while start[position] is not None: position += 1
            start[position] = layout_cell

start = tuple((cell, False) for cell in start)
print(explore(start))
