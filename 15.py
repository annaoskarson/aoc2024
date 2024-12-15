import time

data = [row.split() for row in open('15.txt').read().strip().split('\n\n')]

walls = set()
boxes = set()
walls2 = set()
boxes2 = {}

rmax = 0
cmax = 0
for r, row in enumerate(data[0]):
    c = 0
    while c < len(row):
        if data[0][r][c] == '#':
            walls.add((r,c))
            walls2.add( (r,c*2) )
            walls2.add( (r,c*2 + 1) )
        elif data[0][r][c] == 'O':
            boxes.add((r,c))
            boxes2[(r,c*2)] = '['
            boxes2[(r, c*2+1)] = ']'
        elif data[0][r][c] == '@':
            bot = (r,c)
            bot2 = (r,c*2)
        c += 1

rows = range(r+1)
cols = range(c+1)

rows2 = range(r+1)
cols2 = range(2*c)

thewalk = ''.join(data[1])
   
def pprint():
    image = ''
    for r in rows:
        row = ''
        for c in cols:
            if (r,c) in walls:
                row += '#'
            elif (r,c) in boxes:
                row += 'O'
            elif (r,c) == bot:
                row += '@'
            else:
                row += '.'
        image += row + '\n'
    print(image)
    time.sleep(0.05)

def pprint2():
    image = ''
    for r in rows2:
        row = ''
        c = 0
        while c in cols2:
            if (r,c) in walls2:
                row += '#'
            elif (r,c) in boxes2:
                row += boxes2[(r,c)]
            elif (r,c) == bot2:
                row += '@'
            else:
                row += '.'
            c += 1
        image += row + '\n'
    print(image)
    time.sleep(0.05)

def walk(s, bot, boxes):
    dirs = ['^', '>', 'v', '<']
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = d[dirs.index(s)]
    nbot = tuple([a+b for a,b in zip(bot, direction)])
    if nbot in walls:
        return(bot, boxes)
    elif nbot in boxes:
        nbox = tuple([a+b for a,b in zip(nbot, direction)])
        while nbox not in walls:
            if nbox not in boxes:
                boxes.remove(nbot)
                boxes.add(nbox)
                return(nbot, boxes)
            nbox = tuple([a+b for a,b in zip(nbox, direction)])
    else:
        return(nbot, boxes)
    return(bot, boxes)

def pushboxes(bot, direction, boxes):
    affected = {}
    nspot = tuple([a+b for a,b in zip(bot, direction)])
    
    if direction[0] == 0:
        # move on row
        while nspot in boxes:
            affected[nspot] = boxes[nspot]
            nspot = tuple([a+b for a,b in zip(nspot, direction)])
        if nspot in walls2:
            return(bot, boxes)

    else:
        q = [nspot]
        while q:
            this = q.pop(0)
            if this not in affected:
                affected[this] = boxes[this]

                if boxes[this] == '[':
                    other = ( this[0], this[1] +1 )
                else:
                    other = ( this[0], this[1] -1 )
                if other not in affected:
                    q.append(other)

                newone = tuple([a+b for a,b in zip(this, direction)])
                if newone in walls2:
                    return(bot, boxes)
                elif newone in boxes.keys():
                    q.append(newone)
    
    # could move
    for move in affected:
        boxes.pop(move)
    for move in affected:
        newspot = tuple([a+b for a,b in zip(move, direction)])
        boxes[newspot] = affected[move]
    
    # also, move the bot
    nbot = tuple([a+b for a,b in zip(bot, direction)])

    return(nbot, boxes)
        
def walk2(s, bot, boxes):
    dirs = ['^', '>', 'v', '<']
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = d[dirs.index(s)]
    nbot = tuple([a+b for a,b in zip(bot, direction)])
    if nbot in walls2:
        return(bot, boxes)
 
    elif nbot in boxes:
        bot, boxes = pushboxes(bot, direction, boxes)
        return(bot, boxes)
 
    else:
        return(nbot, boxes)

# Part 1
for w in thewalk:
    (bot, boxes) = walk(w, bot, boxes)
    #pprint()

pprint()
score = sum([100 * b[0] + b[1] for b in boxes])
print('Part 1:', score)

# Part 2
#pprint2()
print(bot2)
for w in thewalk:
    #print('Move', w)
    (bot2, boxes2) = walk2(w, bot2, boxes2)
    #pprint2()
pprint2()

score = 0
for r in rows2:
    c = 0
    for c in cols2:
        if (r,c) in boxes2 and boxes2[(r,c)] == '[':
            score += 100 * r + c

print('Part 2:', score)
