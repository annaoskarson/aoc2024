data = [int(ch) for ch in (open('09.txt')).read().strip()]

def readfs(d = data):
    fs = []
    i = 0
    fid = 0
    isfile = 1
    while i < len(d):
        if isfile:
            fs = fs + [fid]*d[i]
            #file = data[i]
            fid += 1
            isfile = 0
        else:
            fs = fs + [None]*d[i]
            #free = data[i+1]
            isfile = 1
        i += 1
    return(fs)

def pprint(fs):
    # Prints digits for the shorter examples.
    #print(''.join([str(f) if f != None else '.' for f in fs]))
    row = ''
    for f in fs:
        if f == None:
            row += '.'
        elif f < 10:
            row += str(f)
        else:
            row += 'X'
    print(row)
    #print(''.join(['X' if f != None else '.' for f in fs]))

def findlastpos(fs):
    last = len(fs)-1
    while fs[last] == None:
        last -=1
    return(last)
#pprint(fs)

def pack(fs):
    last = findlastpos(fs)
    # pack:
    i = 0
    while i < last:
        #pprint(fs)
        if fs[i] == None:
            while fs[last] == None:
                last -= 1
            fs[i] = fs[last]
            fs[last] = None
            last -= 1
        i += 1
    return(fs)

def filesystem(fs):
    files = {}
    space = {}
    fids = {}
    i = 0
    while i < len(fs):
        if fs[i] == None:
            # Start of space!
            startpos = i
            while i < len(fs) and fs[i] == None:
                i += 1
            length = i-startpos
            space[startpos] = length
        else:
            # Start of file!
            startpos = i
            fid = fs[i]
            while i < len(fs) and fs[i] == fid:
                i += 1
            length = i-startpos
            files[startpos] = (length, fid)
            fids[fid] = (startpos, length)
    return(files, space, fids)

def checksum(fs):
    cs = 0
    i = 0
    while i < len(fs):
        if fs[i] != None:
            cs += (i*fs[i])
        i += 1
    return(cs)

# Part 2

def advanced_read(d = data):
    files = {}
    space = {}
    fids = {}
    i = 0
    pos = 0
    isfile = True
    fid = 0
    for length in d:
        if isfile:
            files[pos] = (length, fid)
            fids[fid] = (pos, length)
            fid += 1
            pos += length
            isfile = False
        else:
            space[pos] = length
            pos += length
            isfile = True        
    return(files, space, fids)

def fpack(files, space, fids):
    for thefid in sorted(list(fids.keys()), reverse=True):
        fstart, flength = fids[thefid]

        for sstart in sorted(list(space.keys())):
            if sstart >= fstart: # Don't move to the right!
                break
            slength = space[sstart]
            diff = slength - flength
            if diff >= 0: # There is space enough.
                files.pop(fstart)
                space.pop(sstart)
                
                files[sstart] = (flength, thefid)
                fids[thefid] = (sstart, flength)
                if diff > 0:
                    space[sstart+flength] = diff
                break
    return(files, space, fids)

def advanced_print(files, space):
    # Prints digits for the shorter examples.
    row = ''
    end = max((list(space.keys())+ list(files.keys())))
    for pos in range(end + 1):
        if pos in files.keys():
            length, fid = files[pos]
            if fid > 9:
                row += 'X'*length
            else:
                row += str(fid)*length
        elif pos in space.keys():
            length = space[pos]
            row += '.'*length
    print(row)
    return(row)

def advanced_checksum(files):
    checksum = 0
    for start in files.keys():
        length, fid = files[start]
        for pos in range(start, start+length):
            checksum += pos * fid
    return(checksum)

# Part 1
fs = readfs()
pprint(fs)
nfs = pack(fs)
#print()
pprint(nfs)
print('Part 1:', checksum(nfs))

# Part 2
files, space, fids = advanced_read()
advanced_print(files, space)
print()
files2, space2, fids2 = fpack(files, space, fids)
advanced_print(files2, space2)

print('Part 2:', advanced_checksum(files2))