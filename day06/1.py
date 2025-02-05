import sys
import re

file="input.txt"

f = open(file)

times=[]
dists=[]
for line in f.readlines():
    match=re.match(r'Time:\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)',line)
    if match:
        for i in match.groups():
            times.append(int(i))
    match=re.match(r'Distance:\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)',line)
    if match:
        for i in match.groups():
            dists.append(int(i))

score=1
for i in range(len(times)):
    thisscore=0
    print(f'time:{times[i]} dist:{dists[i]}')
    for button in range(times[i]):
        thisdist=(times[i]-button)*(button)
        if thisdist>dists[i]:
            thisscore+=1
    score*=thisscore

print(score)
