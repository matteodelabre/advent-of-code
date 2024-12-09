def safe(report):
    return (
        (report == sorted(report) or report[::-1] == sorted(report))
        and all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    ) 

def subsafe(report):
    return (
        safe(report)
        or any(safe(report[:i] + report[i+1:]) for i in range(len(report)))
    )

print(sum(
    subsafe(list(map(int, line.split())))
    for line in open(0)
))
