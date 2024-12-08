themap = [[ch for ch in row] for row in (open('08.txt')).read().split('\n') if len(row) > 0]

def pprint(antinodes, antennap):
    image = ''
    for r in range(len(themap)):
        row = ''
        for c in range(len(themap[r])):
            if (r,c) in antinodes:
                row += '#'
            elif (r,c) in antennap.keys():
                row += antennap[(r,c)]
            else:
                row += '.'
        image += row + '\n'
        row = ''
    print(image + '\n')

# Prepare the data.
antinodes1 = set() # Part 1
antinodes2 = set() # Part 2
antennas = {} # Antenna positions, based on antenna types
antennap = {} # Antenna positions, based on points on map
for r, row in enumerate(themap):
    for c, ch in enumerate(row):
        if ch not in ['.', '#']:
            antennap[(r,c)] = ch
            if ch not in antennas:
                antennas[ch] = []
            antennas[ch].append((r,c))

# Solve
for p in [(r,c) for r in range(len(themap)) for c in range(len(themap[0]))]:
    for ant in antennas.keys():
        positions = antennas[ant]
        # Part 1:
        if (any([(p[0]-a[0] == 2*(p[0]-b[0])) and (p[1]-a[1] == 2*(p[1]-b[1]) and a != b) for a in positions for b in positions])):
            antinodes1.add(p)
        # Part 2:
        for i, a in enumerate(antennas[ant]):
            for b in antennas[ant][i+1:]:
                if (a[1] == p[1] == b[1]) or (a[0] == p[0] == b[0]): # same column or row
                    print('never occurs')
                    antinodes2.add(p)
                elif (p == a) or (p == b): # we are on an antenna.
                    antinodes2.add(p)
                elif a[1] - p[1] == 0 or b[1] - p[1] == 0 or a[0] - p[0] == 0 or b[0] - p[0] == 0:
                    # one of the antennas is on same row or column but not the other antenna
                    pass
                elif ((a[0] - p[0]) / (a[1] - p[1])) == ((b[0] - p[0]) / (b[1] - p[1])):
                    antinodes2.add(p)

pprint(antinodes1, antennap)
print((len(antinodes1)))

pprint(antinodes2, antennap)
print((len(antinodes2)))