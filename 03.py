# pydroid on phone, on the bus to work
import re

data = (open('03.txt')).read()

#print(data)
#apa = re.findall('mul(\d+,\d+)', data)
mul = 'mul\(\d+\,\d+\)'
apa = re.findall(mul, data)

#print(apa)
cepa = 0

for ap in apa:
    bepa = list(map(int, re.findall('\d+', ap)))
    #print(bepa)
    cepa += bepa[0]*bepa[1]
    
print(cepa)
#do = 'do[n\'t]?\(\)'
do = 'do(?:n\'t)?\(\)'
domul = mul +'|' + do

newapa = re.findall(domul, data)
#print(newapa)

on = True
depa = 0
for na in newapa:
    if "t(" in na:
        on = False
    elif 'do()' in na:
        on = True
    elif on:
         bepa = list(map(int, re.findall('\d+', na)))
         depa += int(bepa[0])*int(bepa[1])
        
print('\n')
print(depa)