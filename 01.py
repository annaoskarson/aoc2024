data = [(r.strip()).split(' ') for r in open('01.txt')]

left = [int(d[0]) for d in data]
right = [int(d[-1]) for d in data]

# distance
distance = sum([abs(l-r) for (l,r) in zip(sorted(left),sorted(right))])

# similarity score
similarity = sum([right.count(l)*l for l in left])        

print('Part 1:', distance)
print('part 2:', similarity)