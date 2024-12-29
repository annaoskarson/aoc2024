
reg = {}
for r,row in enumerate(open('17.txt').read().strip().split('\n')):
    if 'Register' in row:
        a,b = row.split(':')
        reg[a.split()[1]] = int(b)
    elif 'Program' in row:
        instrux = [int(a) for a in row.split()[1].split(',')]

def run(instrux):
    out = []
    i = 0

    while i < len(instrux)-1:

        opcode = instrux[i]
        i += 1
        operand = instrux[i]
        combo = [0, 1, 2, 3, reg['A'], reg['B'], reg['C'], None][operand]
        i += 1

        if opcode == 0:
            # adv
            reg['A'] = reg['A'] // (2**combo)
        
        elif opcode == 1:
            # bxl
            reg['B'] = reg['B'] ^ operand

        elif opcode == 2:
            # bst
            reg['B'] = combo % 8

        elif opcode == 3:
            # jnz
            if reg['A'] != 0:
                i = operand

        elif opcode == 4:
            # bxc
            reg['B'] = reg['B'] ^ reg['C']
        
        elif opcode == 5:
            # out
            out.append(combo % 8)

        elif opcode == 6:
            # bdv
            reg['B'] = reg['A'] // (2**combo)

        elif opcode == 7:
            # cdv
            reg['C'] = reg['A'] // (2**combo)
    return(out)

print('Part 1:', run(instrux))

# Well, I looked at the values and locked in one after one
# of the output digits ...

a = 0o25051
a = 0o1025052 -0o1
a = 0o32025057# - 0o1
a = 0o1025057
# 0o3532025057
# 0o637766025057 (10 siffror)
#a = 0o1726274025057 #(11 siffror)
#a = 0o11726274025057 #(14 siffror)
a = 0o611726274025057 # (15 siffror)
#x = 0
a = 202991746427439
# Had to subtract from here ...
# 202991746427437
# 202991746427434
while True:
    #a = a + 0o1000000000
    #a += 0o1 * x
    reg['A'] = a
    #x += 1

    out = run(instrux)

    test = 14 # when found a value, I 
    if out[:test] == instrux[:test]:
        print('oct a', oct(a))
        print(out)
        print(instrux)
        pass
        if out[:test+1] == instrux[:test+1]:
            print('oct a', oct(a))
            print(out)
            print(instrux)
            input()
        
    if instrux[:len(out)] == out:

        print()
        print(oct(a))
        print(a)
        print(out)
        print(instrux)

        input()

    if instrux == out:
        print(a, 'isTEHshit')
        input()

    a -= 1 # When found an answer, I had to subtract to find the lowest.