import time
data = [[ch for ch in row] for row in open('16.txt').read().strip().split()]

start = next((r,c) for r,row in enumerate(data) for c, ch in enumerate(row) if ch == 'S')
goal = next((r,c) for r,row in enumerate(data) for c, ch in enumerate(row) if ch == 'E')

rows = range(len(data))
cols = range(len(data[0]))

def pprint(way):
    global data
    global scores
    image = ''
    for r, row in enumerate(data):
        for c, ch in enumerate(row):
            if (r,c) in way:
                image += '█'
            else:
                image += ch
        image += '\n'
    print(image)
    time.sleep(0.01)

d = [(-1,0), (0,1), (1,0), (0,-1)]

def walk(here, facing, costtohere, waytohere):
    # Where can we go from here, and what does it cost?
    golist = []
    for turning in [-1, 0, 1]:
        newface = (facing + turning) % 4
        direction = d[newface]
        walkto = (here[0] + direction[0], here[1] + direction[1])
        if data[walkto[0]][walkto[1]] != '#':
            addcost = abs(turning)*1000 + 1
            golist.append((walkto, newface, costtohere + addcost, waytohere + [walkto]))
    return(golist)

def runrudolph(here, facing, cost):
    global data
    global scores
    way = [here]
    ways = set()
    goalcost = float('Inf')
    q = [(here, facing, cost, way)]
    while q:
        here, facing, cost, way = q.pop(0)
        if here == goal and cost <= goalcost:
            goalcost = cost
            ways = ways|set(way)

        goto = walk(here, facing, cost, way)
        if (here, facing) not in scores.keys() or scores[(here, facing)] >= cost:
            scores[(here, facing)] = cost

            for g in goto:
                q.append(g)
            q.sort(key = lambda x: x[2])
    return(goalcost, ways)

scores = {}
cost, ways = runrudolph(start,1,0)

pprint(list(ways))
print('Part 1:', cost)
print('Part 2:', len(ways))



