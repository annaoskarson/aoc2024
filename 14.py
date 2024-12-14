import time

data = [row.split() for row in open('14.txt').read().strip().split('\n')]

#print(data)
rx = 101
ry = 103
#rx = 11
#ry = 7
roomx = range(rx)
roomy = range(ry)

def makebots(data):
    bots = []
    for d in data:
        
        pos = tuple([int(a) for a in d[0].split('=')[1].split(',')])
        vel = tuple([int(a) for a in d[1].split('=')[1].split(',')])
        bots.append((pos, vel))
    return(bots)

def walkbot(bot):
    #print(bot)
    p, vel = bot
    p1 = (p[0] + vel[0]) % rx, (p[1] + vel[1]) % ry
    return((p1, vel))

def scoring(bots):
    q1x = range(0, rx // 2)
    q1y = range(0, ry // 2)
    q1 = [(x,y) for x in q1x for y in q1y]
    q2x = range(rx // 2 + 1, rx)
    q2y = range(0, ry // 2)
    q2 = [(x,y) for x in q2x for y in q2y]
    q3x = range(0, rx // 2)
    q3y = range(ry // 2 + 1, ry)
    q3 = [(x,y) for x in q3x for y in q3y]
    q4x = range(rx // 2 + 1, rx)
    q4y = range(ry // 2 + 1, ry)
    q4 = [(x,y) for x in q4x for y in q4y]
    score = [0, 0, 0, 0]
    for b in bots:
        p,v = b
        if p in q1:
            score[0] += 1
        elif p in q2:
            score[1] += 1
        elif p in q3:
            score[2] += 1
        elif p in q4:
            score[3] += 1
    total = score[0] * score[1] * score[2] * score[3]
    return(total)
        
def pprint(tbots):
    bots = [p for (p,v) in tbots]
    image = ''
    for y in roomy:
        row = ''
        for x in roomx:
            nbr = bots.count((x,y))
            if nbr > 0:
                row += str(nbr)
            else:
                row += '.'
        image += row + '\n'
    print(image)
    time.sleep(0.1)

def istree(bots):
    # Well, it is a bit hard to detect a tree. It might be big and dense ...
    # But when you know, you know ...
    treebot = []
    def nbs(bot):
        (x,y),_ = bot
        nbs = [(x1, y1) for x1 in [x-1, x, x+1] for y1 in [y-1, y, y+1] if (x1, y1) != (x,y) and x1 in roomx and y1 in roomy]
        nbsb = [p for p in nbs for (p1,_) in bots if p == p1] 
        return(len(nbsb))
    
    for bot in bots:
        n = nbs(bot)
        if n >= 7:
            treebot.append(bot)
    score = len(treebot)
    
    return(score >= 10)

bots = makebots(data)
ti = 1000000
t = 0
while True:
    tbots = []
    for bot in bots:
        tbot = walkbot(bot)
        tbots.append(tbot)
    bots = tbots
    #if t+1 == 7847:
    #    pprint(bots)
    #    input()
    #pprint(bots)
    #print(t+1)
    #input()
    if istree(bots):
        pprint(bots)
        print(t+1)
        input('... found something interesting, press enter to continue ...')
        print('continuing')
    if (t+1) % 100 == 0:
        print(t+1) # Just to see the progress.
    if t == 100:
        print('Part 1:', scoring(tbots))
        input('... press enter to continue with part 2 ...')
        print('continuing')

    t += 1
