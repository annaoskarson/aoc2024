garden = {}
for r,row in enumerate(open('12.txt').read().strip().split()):
    for c,ch in enumerate(row):
        garden[(r,c)] = ch

rownbrs = range(r+1)
colnbrs = range(c+1)

def prettyprint():
    import time
    global garden
    global fenced
    image = ''
    for r in rownbrs:
        row = ''
        for c in colnbrs:
            if (r,c) in fenced:
                #row += garden[(r,c)].lower()
                row += '.'
            else:
                row += garden[(r,c)]
        image += row + '\n'
    print(image)
    time.sleep(0.05)

def fill(p):
    global fenced
    plant = garden[p]
    q = [p]
    plot = []
    while q:
        this = q.pop(0)
        if this not in fenced:
            plot.append(this)
            fenced.add(this)
            r,c = this
            nbs = [(r1, c1) for (r1, c1) in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)] if (r1 in rownbrs) and (c1 in colnbrs)]
            for n in nbs:
                if n not in fenced and garden[n] == plant:
                    q.append(n)
    return(plot)

fenced = set()
plots = []
for r in rownbrs:
    for c in colnbrs:
        if (r,c) not in fenced:
            #prettyprint()
            plot = fill((r,c))
            plots.append(plot)
    #prettyprint()

price = 0
for plot in plots:
    area = len(plot)
    fence = 0
    for p in plot:
        rp, cp = p
        nbs = [(r1, c1) for (r1, c1) in [(rp-1,cp), (rp+1,cp), (rp,cp-1), (rp,cp+1)] if (r1 in rownbrs) and (c1 in colnbrs) and (r1,c1) in plot]
        fence += (4-len(nbs))
    price += area * fence

print('Part 1:', price)

def sides(plot):
    pc = 0
    minr = min(r for r,c in plot)
    maxr = max(r for r,c in plot)
    minc = min(c for r,c in plot)
    maxc = max(c for r,c in plot)

    for r in range(minr-1, maxr+1):
        for c in range(minc-1, maxc+2):
            look = ((r,c), (r+1,c), (r+1,c+1), (r,c+1))
            inside = [p in plot for p in look]
            if sum(inside) in [1,3]:
                pc += 1
            elif inside == [True, False, True, False] or inside == [False, True, False, True]:
                pc += 2
    return(pc)

price = 0
for plot in plots:
    s = sides(plot)
    price += s * len(plot)

print('Part 2:', price)
