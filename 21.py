codes = open('21.txt').read().strip().split()

class Bot():
    def __init__(self, name):
        self.name = name

    def coords_of(self, button): # The position of the button with the "button" on.
        pos  = [i for i in self.keypad if self.keypad[i] == button][0]
        return(pos)

    def pointing(self): # What button I point at.
        return(self.keypad[self.pos])

    def step(self,inst): # Perform an action according to instruction.
        if inst == '':
            return('')
        if inst == 'A':
            return(self.press())
        if inst == '^':
            d = (-1,0)
        elif inst == '>':
            d = (0,1)
        elif inst == 'v':
            d = (1,0)
        elif inst == '<':
            d = (0,-1)
        newpos = (self.pos[0] + d[0], self.pos[1] + d[1])
        if (newpos) in self.keypad.keys():
            self.pos = newpos
        else:
            assert False, "Panic!"
        return('')

    def press(self): # Press the button pointing at.
        return(self.keypad[self.pos])
    
    def check(self, way): # Check if a path is valid.
        prepos = self.pos
        for w in way:
            try:
                self.step(w)
            except:
                self.pos = prepos
                return(False)
        self.pos = prepos #was just checking ... Didn't want to move for real. :-)
        return(True)

    def go_to_press(self, button):

        pos_start = self.pos
        pos_end = self.coords_of(button)

        ways = []
        p = ''
        v = pos_end[0] - pos_start[0]
        h = pos_end[1] - pos_start[1]

        if v > 0: ch = 'v'
        else: ch = '^'
        p += ch*abs(v)
        if h > 0: ch = '>'
        else: ch = '<'
        p += ch*abs(h)
        q = p[::-1]
        if p != q:
            if self.check(p):
                ways.append(p + 'A')
            if self.check(q):
                ways.append(q + 'A')
        else:
            ways.append(p + 'A')

        self.pos = pos_end
        return(ways)

    def look(self, ch): # Check what's next to the current button, in a certain direction.
        chs = ['v', '^', '>', '<']
        d = [(1,0), (-1,0), (0,1), (0,-1)][chs.index(ch)]
        l = (self.pos[0] + d[0], self.pos[1] + d[1])
        return(l)

class Numbot(Bot):
    keypad = {}
    keypad[(0,0)] = '7'
    keypad[(0,1)] = '8'
    keypad[(0,2)] = '9'
    keypad[(1,0)] = '4'
    keypad[(1,1)] = '5'
    keypad[(1,2)] = '6'
    keypad[(2,0)] = '1'
    keypad[(2,1)] = '2'
    keypad[(2,2)] = '3'
    #keypad[(3,0)] = None
    keypad[(3,1)] = '0'
    keypad[(3,2)] = 'A'

    def reset(self):
        self.pos = (3,2)

    def __init__(self, name):
        super().__init__(name)
        self.pos = (3,2)

    def __repr__(self):
        point = self.keypad[self.pos]
        image = '\n' + self.name + ':\n+---+---+---+\n|'
        if point == '7': image += '░7░'
        else: image += ' 7 '
        image += '|'
        if point == '8': image += '░8░'
        else: image += ' 8 '
        image += '|'
        if point == '9': image += '░9░'
        else: image += ' 9 '
        image += '|\n+---+---+---+\n|'
        if point == '4': image += '░4░'
        else: image += ' 4 '
        image += '|'
        if point == '5': image += '░5░'
        else: image += ' 5 '
        image += '|'
        if point == '6': image += '░6░'
        else: image += ' 6 '
        image += '|\n+---+---+---+\n|'
        if point == '1': image += '░1░'
        else: image += ' 1 '
        image += '|'
        if point == '2': image += '░2░'
        else: image += ' 2 '
        image += '|'
        if point == '3': image += '░3░'
        else: image += ' 3 '
        image += '|\n+---+---+---+\n    |'
        if point == '0': image += '░0░'
        else: image += ' 0 '
        image += '|'
        if point == 'A': image += '░A░'
        else: image += ' A '
        image += '|\n    +---+---+'
        return(image)
        #+---+---+---+
        #| 7 | 8 | 9 |
        #+---+---+---+
        #| 4 | 5 | 6 |
        #+---+---+---+
        #| 1 | 2 | 3 |
        #+---+---+---+
        #    | 0 | A |
        #    +---+---+

class Dirbot(Bot):
    keypad = {}
    #keypad[(0,0)] = None
    keypad[(0,1)] = '^'
    keypad[(0,2)] = 'A'
    keypad[(1,0)] = '<'
    keypad[(1,1)] = 'v'
    keypad[(1,2)] = '>'

    def reset(self):
        self.pos = (0,2)

    def __init__(self, name):
        super().__init__(name)
        self.pos = (0,2)

    def __repr__(self):
        point = self.keypad[self.pos]
        image = '\n' + self.name + ':\n    +---+---+\n    |'
        if point == '^': image += '░^░'
        else: image += ' ^ '
        image += '|'
        if point == 'A': image += '░A░'
        else: image += ' A '
        image += ''
        image += '|\n+---+---+---+\n|'
        if point == '<': image += '░<░'
        else: image += ' < '
        image += '|'
        if point == 'v': image += '░v░'
        else: image += ' v '
        image += '|'
        if point == '>': image += '░>░'
        else: image += ' > '
        image += ''
        image += '|\n+---+---+---+'
        return(image)
        #    +---+---+
        #    | ^ | A |
        #+---+---+---+
        #| < | v | > |
        #+---+---+---+

def pprint(bots): # Print the bots!
    import time
    for bot in bots:
        image = repr(bot)
        print(image)
    print('\n')
    time.sleep(0.5)

def initbots(many = 2): # Initialize some bots.
    bots = []
    bots.append(Numbot('Bot 1, controlling the numeric '))
    for b in range(many):
        bots.append(Dirbot('Bot ' + str(b+2) + ', controlling bot ' + str(b+1) + ' '))
    return(bots)

def mypress(button, bots): # I press a button, and get a visual result.
    for bthis in bots:
        button = bthis.step(button)
    pprint(bots)
    return(button)

example = {}
example['029A'] = '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'
example['980A'] = '<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A'
example['179A'] = '<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'
example['456A'] = '<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A'
example['379A'] = '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'
examplecodes = ['029A', '980A', '179A', '456A', '379A']

#codes = example.keys() # To run the examples!
instrux = []

bots = initbots(2)
pprint(bots)

#print(bots[1].name)
#exit()
# Trickle down the codes through the layers of bots.
# Return shortest code from the last bot. Add to the other codes ...
memory = {}
def solve(code, bots):
    if len(bots) <= 0:
        return(code)
    b = bots[0]
    if (code, b.name) in memory.keys():
        return(memory[(code,b.name)])
    ans = ''
    for c in code:
        controls = b.go_to_press(c)
        res = []
        for com in controls:
            result = solve(com, bots[1:])
            if len(result) > 0:
                res.append(result)
        shortest = min(res, key=len)
        ans += shortest

    memory[(code, b.name)] = ans
    return(ans)

memory = {}
def solve_num(code, bots):
    if len(bots) <= 0:
        return(len(code))
    b = bots[0]
    if (code, b.name) in memory.keys():
        #print('using mem', (code, b.name), memory[(code,b.name)])
        #input()
        return(memory[(code,b.name)])
    ans = 0
    for c in code:
        #print('processing', c)
        #print('mem', len(memory))
        #print(memory)
        #input()
        controls = b.go_to_press(c)
        res = []
        for com in controls:
            result = solve_num(com, bots[1:])
            if result > 0:
                res.append(result)
        shortest = min(res)
        ans += shortest
    #print('ans', ans)

    memory[(code, b.name)] = ans
    return(ans)

outputs = []
complexity = 0
for code in codes:
    #print('processing', code)
    #print('mem', len(memory))
    #presses = solve(code, bots)
    presses = solve(code, bots)
    theshit = ''.join(presses)
    instrux.append(theshit)
    
    #print('ex',example[code])
    #print('my',theshit)
    stuff = len(theshit)
    stuff2 = int(code[:-1])
    complexity += stuff*stuff2
    print(stuff, '*', stuff2, '=', stuff*stuff2)

#print('68 * 29, 60 * 980, 68 * 179, 64 * 456, and 64 * 379')
#print('= 126384')
print('Part 1:', complexity)
input('... press enter to continue to part 2 ...')

memory = {}
bots = initbots(25)

complexity = 0
for code in codes:
    #print('processing', code)
    #print('mem', len(memory))
    #presses = solve(code, bots)
    presses = solve_num(code, bots)
    #print(presses)
    #theshit = ''.join(presses)
    #instrux.append(theshit)
    
    #print('ex',example[code])
    #print('my',theshit)
    stuff = presses
    stuff2 = int(code[:-1])
    complexity += stuff*stuff2
    print(stuff, '*', stuff2, '=', stuff*stuff2)

# 63740439823140 too low
print('Part 2:', complexity)
ok = input('... press a to continue simulating part 1...')

#print('68 * 29, 60 * 980, 68 * 179, 64 * 456, and 64 * 379')
#print('= 126384')


if ok != 'a':
    exit()

# 257428 too high
# 261392 ...

# And now thesting the code!
bots = initbots(2)

for num,one in enumerate(instrux):
    result = []
    print(one)
    pprint(bots)
    #facit = example[examplecodes[num]]
    for j,i in enumerate(one):
        #if i != facit[j]:
        #    pass
        apa = mypress(i, bots[::-1])
        result += apa
        if len(apa) > 0:
#            print(examplecodes[num])
            print(codes[num])
            print('output:', ''.join(result))
            input('... waiting for keypress ...')
        