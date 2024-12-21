maze = set([(r,c) for r,row in enumerate(open('20.txt').read().strip().split()) for c,ch in enumerate(row) if ch == '#'])

rows = range(len(open('20.txt').read().strip().split()))
cols = range(len(open('20.txt').read().strip().split()[0]))

start = [(r,c) for r,row in enumerate(open('20.txt').read().strip().split()) for c,ch in enumerate(row) if ch == 'S'][0]
goal = [(r,c) for r,row in enumerate(open('20.txt').read().strip().split()) for c,ch in enumerate(row) if ch == 'E'][0]

def pprint(maze, start, goal, way = [], cheatway = []):
    import time
    image = ''
    for r in rows:
        for c in cols:
            if (r,c) in cheatway:
                image += '░'
            elif (r,c) in maze:
                image += '#'
            elif (r,c) in way:
                image += '█'
            elif (r,c) == start:
                image += 'S'
            elif (r,c) == goal:
                image += 'E'
            else:
                image += '.'
        image += '\n'
    print(image)
    time.sleep(0.001)

ff = {}
def race(maze, start, goal):
    q = [(start, 0, [])]
    seen = set()
    while q:
        here, steps, way = q.pop(0)
        if here == goal:
            return(steps, way)
        seen.add(here)        
        nbs = [n for n in [(here[0], here[1]+1), (here[0], here[1]-1), (here[0]+1, here[1]), (here[0]-1, here[1])] if n not in maze]
        for n in nbs:
            if n not in seen:
                q.append((n, steps + 1, way + [here]))
        q.sort(key=lambda tup: tup[1])
    return(steps, way)

original, way = race(maze, start, goal)

pprint(maze, start, goal, way)

way += [goal]

cheats = 0
saved = {}
for cheat in maze:
    if cheat[0] in [0, max(rows)] or cheat[1] in [0, max(cols)]:
        continue
    nbs = [n for n in [(cheat[0]+1, cheat[1]), (cheat[0]-1, cheat[1]), (cheat[0], cheat[1]-1), (cheat[0], cheat[1]+1)] if n not in maze]
    saved = 0
    apa =[abs(way.index(n1)-way.index(n2))-1 for n1 in nbs for n2 in nbs[1:] if n1 != n2]
    if len(apa) > 0:
        saved = max(apa)
    if saved >= 100:
        cheats += 1

print('Part 1:', cheats)

cheatways = {}
saved = {}
def cheatfinder(maze, way, begin):
    seen = set()
    q = [(begin, [])]
    while q:
        this, cheatway = q.pop(0)
        if len(cheatway) > 20:
            continue
        if this in seen:
            continue
        if this in way or this == goal:
            seen.add(this)
            save = abs(way.index(this) - way.index(begin)) - (abs(this[0] - begin[0]) + abs(this[1] - begin[1]))
            if save >= 100:
                if (begin, this) not in cheatways:
                    if save not in saved.keys(): # For the example
                        saved[save] = 0
                    saved[save] += 1
                    #pprint(maze, start, goal, way, cheatway + [this])
                    #input()
                    cheatways[(begin,this)] = cheatway + [this]
 
        nbs = [n for n in [(this[0]+1, this[1]), (this[0]-1, this[1]), (this[0], this[1]-1), (this[0], this[1]+1)] if n[0] in rows and n[1] in cols]

        for n in nbs:
            q.append((n, cheatway+[this]))
        seen.add(this)


for trying in way:
    pprint(maze, start, goal, [trying])
    cheatfinder(maze, way, trying)

#print(saved) # For the example

print('Part 2:', len(list(cheatways.keys()))//2)
# Because both genvägar and senvägar is recorded, the amount must be halved.
