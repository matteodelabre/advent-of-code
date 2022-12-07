dirsizes = {(): 0}
curpath = ()

for line in open(0):
    match line.split():
        case ["$", "cd", ".."]:
            curpath = curpath[:-1]

        case ["$", "cd", move]:
            curpath += (move,)
            dirsizes[curpath] = 0

        case ["$", "ls"] | ["dir", _]: pass

        case [size, file]:
            for i in range(len(curpath) + 1):
                dirsizes[curpath[:i]] += int(size)

print(min(
    size for size in dirsizes.values()
    if size >= dirsizes[()] - 40000000
))
