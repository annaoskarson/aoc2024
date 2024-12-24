towels, designs = open('19.txt').read().strip().split('\n\n')

towels = [t.strip() for t in towels.split(',') if len(t) > 0]
designs = designs.split()

def designer(towels, design, impossible):
    if len(design) == 0:
        return(True)
    if len(design) not in impossible:
        for t in towels:
            if design.startswith(t) and len(t) <= len(design):
                if designer(towels, design[len(t):], impossible):
                    return(True)
    impossible.add(len(design))
    return(False)

def improved_designer(towels, design, possible, ways):

    if design in ways.keys():
        return(ways[design])
    if len(design) == 0:
        return(1)
    numways = 0
    for t in towels:
        if design.startswith(t) and len(t) <= len(design):
            numways += improved_designer(towels, design[len(t):], possible, ways)
            if design not in ways.keys():
                ways[design] = 0
            ways[design] = numways

    return(numways)


possible = 0
for i,d in enumerate(designs):
    possible += designer(towels, d, set())

print('Part 1:', possible)

ways = 0
for i,d in enumerate(designs):
    this = improved_designer(towels, d, set(), {})
    ways += this

print('Part 2:', ways)


def other_designer(towels, design):
    unsolvable = set()
    q = set()
    q.add(design)
    while q:
        design = q.pop()
        if len(design) == 0:
            return(True)
        if design not in unsolvable:
            for t in towels:
                if design.startswith(t) and len(t) <= len(design):
                    q.add(design[len(t):])
    #unsolvable.add(design)
    return(False)

possible = 0
for i,d in enumerate(designs):
    possible += other_designer(towels, d)

print('Part 1, alternative solution:', possible)

def superduperdesigner(towels, design):
    unsolvable = set()
    ways = 0
    q = set()
    q.add(design)
    while q:
        this = q.pop()
        if len(this) == 0:
            ways += 1
        for t in towels:
            if this.startswith(t) and len(t) <= len(this):
                q.add(this[len(t):])
    return(ways)

# if apa in queue, add 1 to apa in the queue.
#  q = {('apapapap', 3), ('papapap', 5), ('', 10)}
# When appending, just append one if many (like a set), but add how many you added
# --- Think about it.
# When solved, note the numbers added up in some way ...

ways = 0
for i,d in enumerate(designs):
    this = superduperdesigner(towels, d)
    ways += this

print('Part 2, alternative solution:', ways)

