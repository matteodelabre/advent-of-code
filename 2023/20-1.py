from collections import deque, defaultdict

flip = set()
conj = set()
outputs = {}
inputs = defaultdict(set)

for line in open(0).read().splitlines():
    name, targets = line.split(" -> ")
    targets = targets.split(", ")

    if name.startswith("%"):
        name = name.removeprefix("%")
        flip.add(name)

    if name.startswith("&"):
        name = name.removeprefix("&")
        conj.add(name)

    outputs[name] = targets

    for target in targets:
        inputs[target].add(name)

repeats = 1_000
sent = {False: 0, True: 0}
flip_state = {name: False for name in flip}
conj_state = {name: {inpt: False for inpt in inputs[name]} for name in conj}

for _ in range(repeats):
    pulses = deque([("button", False, "broadcaster")])

    while pulses:
        start, kind, end = pulses.popleft()
        sent[kind] += 1
        send = None

        if end == "broadcaster":
            send = kind

        elif end in flip:
            if not kind:
                flip_state[end] = not flip_state[end]
                send = flip_state[end]

        elif end in conj:
            conj_state[end][start] = kind
            send = not all(state for state in conj_state[end].values())

        if send is not None:
            for out in outputs[end]:
                pulses.append((end, send, out))

print(sent[False] * sent[True])
