def safe(report):
    return (
        (report == sorted(report) or report[::-1] == sorted(report))
        and all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    ) 

print(sum(
    safe(list(map(int, line.split())))
    for line in open(0)
))
