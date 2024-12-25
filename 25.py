
things = [t for t in open('25.txt').read().strip().split('\n\n')]

locks = []
keys = []

for t in things:
    t = t.split('\n')
    pins= {}
    for col in range(len(t[0])):
        pins[col] = sum([ch == '#' for r in range(len(t)) for ch in t[r][col]])-1

    if all([ch == '#' for ch in t[0]]):
        locks.append(pins)
    else:
        keys.append(pins)

def works(key, lock):
    for c in key.keys():
        if lock[c] + key[c] > 5:
            return(False)
    return(True)

pairs = set()
for key in keys:
    for lock in locks:
        if works(key, lock):
            pairs.add((tuple(key.items()), tuple(lock.items())))
            
print('Part 1:', len(pairs))

