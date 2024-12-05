data = [r.strip() for r in (open('05.txt')).read().split('\n') if len(r) > 0 ]

look = {}
books = []

for r in data:
    if '|' in r:
        a,b = map(int, r.split('|'))
        if a not in look.keys():
            look[a] = []
        look[a].append(b)
    else:
        books.append([int(c.strip()) for c in r.split(',')])

def valid(book):
    for order, page in enumerate(book):
        if page in look.keys():
            for after in look[page]:
                if after in book[:order]:
                    return(False)
    return(True)

def fix(b):
    if valid(b):
        return(b)
    else:
        for order, page in enumerate (b):
            if page in look.keys():
                for right in look[page]:
                    if right in b[:order]: # begin the slicing!
                        left, rightright = b[:order+1], b[order+1:] # before and after the right part
                        left.remove(right) # remove the right number to put it in after the left number
                        b = left + [right] + rightright
        return(fix(b))


ans1 = 0
ans2 = 0
for book in books:
     if valid(book):
         ans1 += book[len(book)//2]
     else:
         book = fix(book)
         ans2 += book[len(book)//2]        

print(ans1)
print(ans2)