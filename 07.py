data = [r.strip().split(':') for r in (open('07.txt')).read().split('\n') if len(r) > 0 ]

for r,row in enumerate(data):
    values = list(map(int, row[1].split()))
    data[r] = [int(row[0]), values]

def validate(goal, wip, numbers, part=1):
    if wip == goal and len(numbers) == 0:
        return(True)
    elif len(numbers) == 0:
        return(False)
    elif wip > goal:
        return(False)
    else:
        wip1 = wip * numbers[0]
        wip2 = wip + numbers[0]
        if part == 2:
            wip3 = int(str(wip)+str(numbers[0]))
            if validate(goal, wip1, numbers[1:], 2) or validate(goal, wip2, numbers[1:], 2) or validate(goal, wip3, numbers[1:], 2):
                return(True)
        else:
            if validate(goal, wip1, numbers[1:]) or validate(goal, wip2, numbers[1:]):
                return(True)

ans1 = 0
for row in data:
    goal, numbers = row
    if validate(goal, numbers[0], numbers[1:]):
        ans1 += goal

print(ans1)

ans2 = 0
for row in data:
    goal, numbers = row
    if validate(goal, numbers[0], numbers[1:], 2):
        ans2 += goal
print(ans2)