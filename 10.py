topo = [[int(n) for n in row] for row in open('10.txt').read().strip().split()]

def pprint(topo, seen):
    image = ''
    for r, row in enumerate(topo):
        prow = ''
        for c, num in enumerate(row):
            if (r,c) in seen:
                prow += 'W'
            else:
                prow += str(num)
        image += prow + '\n'
    print(image + '\n\n')

rs = range(0, len(topo))
cs = range(0, len(topo[0]))

def walk(goto, part1):
    seen = set()
    ans = 0

    while goto:
        pos = goto.pop(0)
        if not part1 or pos not in seen:
            r, c = pos
            seen.add(pos)
            h = topo[r][c]

            if h == 9:
                ans += 1

            else:
                nbs = [(r1, c1) for (r1, c1) in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)] if (r1 in rs) and (c1 in cs)]
                for n in nbs:
                    rn, rc = n
                    if topo[rn][rc] == h + 1:
                        goto.append(n)
    return(ans)

scores = []
starts = [(r,c) for r in range(len(topo)) for c in range(len(topo[r])) if topo[r][c] == 0]

print('Part 1:', sum([walk([start], True) for start in starts]))
print('Part 2:', sum([walk([start], False) for start in starts]))
