import sys
import re

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

directions=[]
for line in f.readlines():
    match=re.match(r'^([LR])+$',line)
    if match:
        print(match.group(0))
        for c in match.group(0):
            directions.append(c)
    match=re.match(r'(\w+) = \((\w+), (\w+)\)',line)
    if match:
        print (match.group(1),match.group(2),match.group(3))

print (directions)
