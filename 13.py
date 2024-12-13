data = [r.split('\n') for r in open('13.txt').read().strip().split('\n\n')]

class machine():

    def __init__(self, m):
        button_a, button_b, prize = m
        self.ax = int(button_a.split()[2][2:][:-1])
        self.ay = int(button_a.split()[3][2:])
        self.a_cost = 3
        self.bx = int(button_b.split()[2][2:][:-1])
        self.by = int(button_b.split()[3][2:])
        self.b_cost = 1
        self.px = int(prize.split()[1].split('=')[1][:-1])
        self.py = int(prize.split()[2].split('=')[1])

    def mtokens(self):
        # Löste ekvationssystemet ...
        n = (self.py * self.bx - self.by * self.px) / (self.ay * self.bx - self.ax * self.by)
        m = (self.px - n * self.ax) / self.bx
        if n.is_integer() and m.is_integer():
            cost = n*self.a_cost+m
            return(cost)
        else:
            return(False)
     
total = 0
for i,m in enumerate(data):
    claw = machine(m)
    tokens = claw.mtokens()
    if tokens:
        total += tokens
print('Part 1:', int(total))

total = 0
for m in data:
    more = 10000000000000
    claw = machine(m)
    claw.px += more
    claw.py += more
    tokens = claw.mtokens()
    if tokens:
        total += tokens
print('Part 2:', int(total))
