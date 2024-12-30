nums = [int(row) for row in open('22.txt').read().strip().split()]

def mix(val, secret):
    return(val^secret)

def prune(secret):
    return(secret % 16777216)

def multi64(secret):
    return(secret*64)

def div32(secret):
    return(secret//32)

def multi2048(secret):
    return(secret*2048)

def process(secret):

    result = multi64(secret)
    secret = mix(result, secret)
    secret = prune(secret)

    result = div32(secret)
    secret = mix(result, secret)
    secret = prune(secret)

    result = multi2048(secret)
    secret = mix(result, secret)
    secret = prune(secret)

    return(secret)

ans = 0
prices = {}
diffs = {}

pricelist = {}

for n, secret in enumerate(nums):
    diffs[n] = [None]
    i = 0
    prices[n] = []
    pricelist[n] = {}
    while i < 2000:
        secret = process(secret)
        lastdigit = int(str(secret)[-1])
        prices[n].append(lastdigit)
        if i > 0:
            diffs[n].append(prices[n][i] - prices[n][i-1])
        if i > 3:
            if tuple(diffs[n][i-3:i+1]) not in pricelist[n]:
                pricelist[n][tuple(diffs[n][i-3:i+1])] = lastdigit
                # Save as dictionary to speed up the second part.

        i += 1
    ans += secret

print('Part 1:', ans)

sequences = set([ tuple(dif[i+1:i+5]) for dif in diffs.values() for i,_ in enumerate(dif[:-4]) ])
# We don't need to search in sequences that never show up. Thus, making a set of tuples
# from the actual diffs.

sell = {}
for i,sequence in enumerate(sequences):
    sell[sequence] = []

    for n in range(len(nums)):
        if sequence in pricelist[n]:
            sell[sequence].append((pricelist[n][sequence]))

price = 0 
for s,n in sell.items():
    price = max(sum(n), price)

print('Part 2:', price)

