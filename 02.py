rows = [list(map(int, (r.strip().split()))) for r in open('02.txt')]

def safe(ls):
    if len(set(ls)) < len(ls):
        return(False)
    desc = [0 < ls[i]-ls[i+1] <= 3 for i in range(len(ls)-1)]
    asc = [0 < ls[i+1]-ls[i] <= 3 for i in range(len(ls)-1)]
    return(all(desc) or all(asc))

saferows = sum([safe(rows[i]) for i in range(len(rows))])

def dampened(ls):
    if safe(ls):
        return(True)
    j = 0
    while j < len(ls):
        if safe(ls[:j]+ls[j+1:]):
            return(True)
        else:
            j += 1
    return(False)

dampenedrows = sum([dampened(rows[i]) for i in range(len(rows))])

print('Part 1:', saferows)
print('part 2:', dampenedrows)