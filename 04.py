data = [r.strip() for r in (open('04.txt')).read().split('\n') if len(r.strip()) > 0]

def xmases(text):
    matches = text.count('XMAS') + text.count('SAMX')
    return(matches)

def dia1(data):
    r, c = len(data)-1, 0
    diagonals = []    
    while True:
        d = ''
        r1, c1 = r, c
        while c1 < len(data[r]) and r1 < len(data):
            d = d + data[r1][c1]
            c1 += 1
            r1 += 1
        diagonals.append(d)
        d = ''
        
        if r == 0 and c == len(data[r])-1:
            return(diagonals)

        if c == 0 and r > 0:
            r -= 1
        elif r == 0 and c < len(data[r])-1:
            c += 1

def dia2(data):
    r, c = 0, 0
    diagonals = []    
    while True:
        d = ''
        r1, c1 = r, c
        while c1 >= 0 and r1 < len(data) :
            d = d + data[r1][c1]
            c1 -= 1
            r1 += 1
        diagonals.append(d)
        d = ''

        if r == len(data)-1 and c == len(data)-1:
            return(diagonals)
        
        if r == 0 and c < len(data[r])-1:
            c += 1
        elif c == len(data[r])-1:
            r += 1

ans1 = 0
vs, hs = 0, 0
for r, row in enumerate(data):
    h = xmases(row)
    v = xmases(''.join([data[x][r] for x in range(len(data))]))
    vs += v
    hs += h
    ans1 += v+h

d = dia1(data) + dia2(data)
h1 = 0
for r, row in enumerate(d):
    h = xmases(row)
    h1 += h
    ans1 += h

print('Part 1:', ans1)

def x_mas(data, r, c):
    if 0 < r < len(data)-1 and 0 < c < len(data)-1:
        one = data[r-1][c-1] + data[r+1][c+1]
        two = data[r+1][c-1] + data[r-1][c+1]
        if set('MS') == set(one) == set(two):
            return(True)

xmases = 0
for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == 'A':
            if x_mas(data, r, c):
                xmases += 1
print('Part 2:', xmases)