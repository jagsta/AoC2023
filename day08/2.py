import sys
import math
import re

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

maps={}
directions=[]
for line in f.readlines():
    match=re.match(r'^([LR])+$',line)
    if match:
        print(match.group(0))
        for c in match.group(0):
            directions.append(c)
    match=re.match(r'(\w+) = \((\w+), (\w+)\)',line)
    if match:
        maps[match.group(1)]={"L":match.group(2),"R":match.group(3)}
        #print (match.group(1),match.group(2),match.group(3))

print (maps)
print (directions)

n=[]
for node in maps:
    if node[2]=="A":
        n.append(node)
print(n)
cycles=[None] * len(n)
for i,node in enumerate(n):
    print(node)
    count=0
    found=False
    nextn=node
    while not found:
        for d in directions:
            count+=1
            nextn=maps[nextn][d]
            if nextn[2]=="Z":
                cycles[i]=count
                print(count,i,node,nextn)
                found=True

print(cycles)
print(math.lcm(cycles[0],cycles[1],cycles[2],cycles[3],cycles[4],cycles[5]))
