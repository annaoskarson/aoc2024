stones = [int(num) for num in open('11.txt').read().strip().split()]

#print(stones)

def blink(stone):
        
    if stone == 0:
        return([1])
    elif len(str(stone)) % 2 == 0:
        splitat = len(str(stone)) // 2
        s1, s2 = int(str(stone)[:splitat]), int(str(stone)[splitat:])
        return([s1, s2])
    else:
        return([2024*stone])

def blinks(times, stones):
    allstones=[]
    nbr = 0
    
    for stone in stones:
        newstones = [stone]
        for t in range(times):
            onetime = []
            for s in newstones:
                onetime.extend(blink(s))
            newstones = onetime
        #allstones.extend(newstones)
        nbr += len(newstones)
    #return(allstones)
    return(nbr)
        
times = 25

st = blinks(times, stones)
print('Part 1:', st)

# Part 2.

stones = [int(num) for num in open('11.txt').read().strip().split()]

stonetionary = {}

def blinks_improved(timeleft, stone):
    global stonetionary
    result = 0

    if timeleft == 1: # Almost done!
        result += len(blink(stone))
    elif (stone, timeleft) in stonetionary.keys(): # Have already done this.
        result += stonetionary[(stone,timeleft)]
    else: # We are doing it.
        newstones = blink(stone)
        for st in newstones:
            result += blinks_improved(timeleft-1, st)
    stonetionary[(stone, timeleft)] = result
    return(result)

time = 75
manystones = 0
for stone in stones:
    manystones += blinks_improved(time, stone)
print('Part 2:', manystones)

# Just wanted to look at the stonetionary.
print(len(stonetionary.keys()))
print(len(set(stone for stone, _ in stonetionary.keys())))
