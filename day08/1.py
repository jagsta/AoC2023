import sys
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

count=0
n="AAA"
found=False
while not found:
    for d in directions:
        n=maps[n][d]
        count+=1
        if n=="ZZZ":
            found=True

print(count)
