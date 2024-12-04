import re

data = [r.strip() for r in (open('04.txt')).read().split('\n') if len(r.strip()) > 0]

def xmases(text):
    #regexmas = r'XMAS|SAMX'
    #matches = re.findall(regexmas, text)
    #print(matches)
    regexmas = r'XMAS'
    matches = re.findall(regexmas, text)
    regexmas = r'SAMX'
    matches = matches + re.findall(regexmas, text)
    return(len(matches))

def dia1(data):
    r, c = len(data)-1, 0
    diagonals = []    
    while True:
        d = ''
        r1, c1 = r, c
        #print('dia1: r,c:', r, c)
        while c1 < len(data[r]) and r1 < len(data):
            d = d + data[r1][c1]
            c1 += 1
            r1 += 1
        diagonals.append(d)
        #print(d)
        d = ''
        
        if r == 0 and c == len(data[r])-1:
            return(diagonals)

        if c == 0 and r > 0:
            #print('a')
            r -= 1
        elif r == 0 and c < len(data[r])-1:
            #print('b')
            c += 1

def dia2(data):
    r, c = 0, 0
    diagonals = []    
    while True:
        d = ''
        r1, c1 = r, c
        #print('dia2: r,c:', r, c)
        while c1 >= 0 and r1 < len(data) :
            d = d + data[r1][c1]
            #print(r1, c1, d)
            c1 -= 1
            r1 += 1
        diagonals.append(d)
        #print(d)
        d = ''

        if r == len(data)-1 and c == len(data)-1:
            return(diagonals)
        
        if r == 0 and c < len(data[r])-1:
            #print('b')
            c += 1
        elif c == len(data[r])-1:
            r += 1

ans1 = 0
vs, hs = 0, 0
for r, row in enumerate(data):
    h = xmases(row)
    v = xmases(''.join([data[x][r] for x in range(len(data))]))
    #print([data[x][r] for x in range(len(data))])
    #print(''.join([data[x][r] for x in range(len(data))]))
    #print('rows', h)
    #print('cols', v)
    vs += v
    hs += h
    ans1 += v+h

#print(hs, vs)

#print('rows + cols', ans1)

d = dia1(data)
#print('dia1 finished', d)
#print('dia2 finished',dia2(data))
d = d + dia2(data)
#print(d)
h1 = 0
for r, row in enumerate(d):
    h = xmases(row)
    #v = xmases(''.join([d[r][c] for c in range(len(d[r]))]))
    #print('diags', h)
    h1 += h
    ans1 += h

#print('diags', h1)

print(ans1)

def x_mas(data, r, c):
    if 0 < r < len(data)-1 and 0 < c < len(data)-1:
        one = data[r-1][c-1] + data[r+1][c+1]
        two = data[r+1][c-1] + data[r-1][c+1]
        if ('MS' in one or 'SM' in one) and ('MS' in two or 'SM' in two):
            #print(one, two)
            return(True)
        else:
            return(False)
    return(False)

xmases = 0
for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == 'A':
            if x_mas(data, r, c):
                xmases += 1
print(xmases)