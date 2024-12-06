class Bot():
    def __init__(self, borders, obstacles, start, direction):
        self.mapborders = borders
        self.obstacles = obstacles
        self.start = start
        self.direction = direction
        self.seen = {start}
        self.position = start

    def onestep(self, obs):
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        npos = tuple(map(sum, zip(self.position, dirs[self.direction])))
        if npos in self.obstacles or (npos and npos == obs): # Turn right
            self.direction = (self.direction + 1) % 4 #0,1  1,0  0,-1 -1,0
            return(False, False)
        elif npos[0] not in self.mapborders[0] or npos[1] not in self.mapborders[1]: # outside map
            return(False, True) # loop, out
        elif (npos, self.direction) in self.seen: # Loop found!
            return(True, False) # loop, out
        else: # Just walk
            self.position = npos
            self.seen.add((npos, self.direction))
            return(False, False)

    def walk(self, trypos = None):
        loop, out = False, False
        while not(out or loop):
            loop, out = self.onestep(trypos) # -1 if a loop
        return(loop, out)

    def whatseen(self):
        return(self.seen)

    def startpoint(self):
        return(self.start)

    def thepath(self):
        return(set([p[0] for p in self.seen]))

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

# Prepare the data
data = [r.strip() for r in (open('06.txt')).read().split('\n') if len(r) > 0 ]

obstacles = set()
borders = (range(len(data)), range(len(data[0])))
for r, row in enumerate(data):
    for c,ch in enumerate(row):
        if ch == '^':
            start = (r,c)
            direction = 0 #(-1,0)
        elif ch == '#':
            obstacles.add((r,c))

# Part 1, prepararation for part 2.
guard = Bot(borders, obstacles, start, direction)
guard.walk()
#print(guard)
print(len(guard.thepath()))
theseen = guard.whatseen()
thestart = guard.startpoint()

# Part 2, only trying to put obstacles where guard walked in part 1.
tryobstacles = set([p[0] for p in theseen if p[0] != thestart])

loops = 0
for place in tryobstacles:
    guard = Bot(borders, obstacles, start, direction)
    loop, _ = guard.walk(place)
    if loop:
#        print(guard)
        loops += 1
print(loops)
