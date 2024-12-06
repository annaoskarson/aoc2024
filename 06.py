import time
data = [r.strip() for r in (open('06.txt')).read().split('\n') if len(r) > 0 ]

class Bot():
    def __init__(self, themap):
        self.obstacles = set()
        self.seen = set()
        self.mapborders = (range(len(themap)), range(len(themap[0])))
        for r, row in enumerate(themap):
            for c,ch in enumerate(row):
                if ch == '^':
                    self.position = (r,c)
                    self.direction = 0 #(-1,0)
                    self.seen.add(((r,c), self.direction))
                elif ch == '#':
                    self.obstacles.add((r,c))

    def step(self):
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        npos = (self.position[0] + dirs[self.direction][0], self.position[1] + dirs[self.direction][1])
        if npos in self.obstacles:
            self.direction = (self.direction + 1) % 4 #0,1  1,0  0,-1 -1,0
        elif npos[0] not in self.mapborders[0] or npos[1] not in self.mapborders[1]:
            return(len(set([p[0] for p in self.seen])))
        elif (npos, self.direction) in self.seen:
            return(-1)
        else:
            self.position = npos
            self.seen.add((npos, self.direction))

    def placething(self, place):
        self.obstacles.add(place)

    def __str__(self):
        pprint = ''
        for r1 in self.mapborders[0]:
            row = ''
            for c1 in self.mapborders[1]:
                if (r1,c1) in self.obstacles:
                    row += '#'
                elif (r1,c1) in [p[0] for p in self.seen]:
                    row += 'X'
                elif (r1,c1) == self.position:
                    row += (['^', '>', 'v', '<'])[self.direction]
                else:
                    row += '.'
            row += '\n'
            pprint += row
        return(pprint)

def walkthewalk(data, trypos = (-1,-1)):
    guard = Bot(data)
    if trypos != (-1,-1):
        guard.placething(trypos)
    finished = False
    show = False # Turn on to show the walking process.
    while not finished:
        finished = guard.step()
        if show:
            time.sleep(0.03)
            print(guard)
    return(finished)

# Part 1
print(walkthewalk(data))

# Part 2
trylist = []
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] not in ['^', '#']:
            trylist += [(r,c)]

loop = 0
for place in trylist:
    if walkthewalk(data, place) == -1:
        loop += 1
print(loop)
