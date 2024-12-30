pairs = [ b.split('-') for b in open('23.txt').read().strip().split()]

party = {}
for pair in pairs:
    p1, p2 = pair    
    if p1 not in party:
        party[p1] = set([p2])
    if p2 not in party:
        party[p2] = set([p1])
    party[p2].add(p1)
    party[p1].add(p2)

threeparties = []
for pair in pairs:
    p1, p2 = pair

    for pn in party[p1]:
        if pn in party[p2] and set((p1, p2, pn)) not in threeparties:
            threeparties.append(set([p1, p2, pn]))

on_t = [ (a,b,c) for (a,b,c) in threeparties if any((a.startswith('t'), b.startswith('t'), c.startswith('t'))) ]

print('Part 1:', len(on_t))

subparties = [{c} for c in party.keys()] # sets with one computer in each
for c1 in party.keys(): # look at all computers
    for part in subparties: # look in all subparties
        if all(comp in party[c1] for comp in part): # add if connected to all in that subparty
            part.add(c1)

print('Part 2:', ','.join(sorted(max(subparties, key=len)))) # biggest party wins
