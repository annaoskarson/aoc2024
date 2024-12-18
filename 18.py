import time

size = 70

rows = range(size+1)
cols = range(size+1)

start = (0,0)
goal = (size, size)

def pprint(this, way):
    image = ''
    for r in rows:
        for c in cols:
            if (r,c) in way:
                image += 'O'
            elif (r,c) in bytes:
                image += '#'
            elif (r,c) == this:
                image += '@'
            else:
                image += '.'
        image += '\n'
    print(image)
    time.sleep(0.02)

def readbytes():
    # 1024
    bytes = []
    for i,b in enumerate(open('18.txt').read().strip().split('\n')):
        (c,r) = map(int, b.split(','))
        bytes.append((r,c))
    return(bytes)

def solve(bytes):
    q = [(start, 0, [])]
    seen = set()
    while q:
        this, steps, way = q.pop(0)

        if this == goal:
            #pprint(this, way)
            return(steps)

        if this in seen:
            continue

        seen.add(this)
        nbs = [n for n in [(this[0]+1, this[1]), (this[0]-1, this[1]), (this[0], this[1]+1), (this[0], this[1]-1)] if n[0] in rows and n[1] in cols and n not in bytes and n not in seen]

        for n in nbs:
            q.append((n, steps+1, way+[this]))

        #pprint(this, way)
    return(False)

def anyway(bytes):
    q = [(start, 0, [])]
    seen = set()
    while q:
        this, steps, way = q.pop(-1)

        if this == goal:
            #pprint(this, way)
            return(steps)

        if this in seen:
            continue

        seen.add(this)
        nbs = [n for n in [(this[0]+1, this[1]), (this[0]-1, this[1]), (this[0], this[1]+1), (this[0], this[1]-1)] if n[0] in rows and n[1] in cols and n not in bytes and n not in seen]

        for n in nbs:
            q.append((n, steps+1, way+[this]))

        #pprint(this, way)
    return(False)


b = readbytes()
bytes = set(b[:1024])
print('Part 1:', solve(bytes))

#i = 1024
#solved = True
#while solved:
#    bytes = b[:i]
#    #solved = anyway(bytes)
#    solved = solve(bytes)
#    i += 1

#print('Part 2:', b[i-1][::-1])

# Backwards, because it's faster!
#i = len(b)
#solved = False
#while not solved:
#    bytes = set(b[:i])
#    solved = solve(bytes)
#    i -= 1
#
#print(i+1)
#print('Part 2:', b[i+1][::-1])

# Binary search, even faster!
trylow = 1024
tryhigh = len(b)
trymid = (tryhigh - trylow) // 2

while True:
    if trymid == trylow or trymid == tryhigh:
        break
    if solve(set(b[:trymid])):
        trylow = trymid
        trymid = (tryhigh + trymid) // 2 - 1
    else:
        tryhigh = trymid
        trymid = (trymid + trylow) // 2 + 1


i = trymid
print('Part 2:', b[i+1][::-1])




