workflows, parts = open(0).read().split("\n\n")
workflows = {
    workflow.split("{")[0]: workflow.split("{")[1][:-1].split(",")
    for workflow in workflows.splitlines()
}

total = 0

for part in parts.splitlines():
    cur = "in"
    exec(part[1:-1].replace(",", ";"))

    while cur not in "AR":
        workflow = workflows[cur]

        for step in workflow:
            if ":" in step:
                cond, foll = step.split(":")

                if eval(cond):
                    cur = foll
                    break
            else:
                cur = step
                break

    if cur == "A":
        total += x + m + a + s

print(total)
