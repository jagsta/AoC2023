import sys
from collections import deque
import re

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

seeds=[]
maps=[]
mapindex=-1
with open(file) as f:
    for line in f.readlines():
        string=re.match(r'(\d+)\s(\d+)\s(\d+)',line)
        if string:
            base=int(string.group(2))
            target=int(string.group(1))
            size=int(string.group(3))
            delta=target-base
            end=base+size-1
            maps[mapindex].add((base,end,delta))
        string=re.match(r'[\w\s-]*(\w+:)',line)
        if string and string.group()=='seeds:':
            print(f'matched seeds: {line}')
            for num in line.rstrip("\n").split():
                if num.isdigit():
                    seeds.append(int(num))
        elif string:
            print(f'matched map: {line}')
            mapindex+=1
            maps.append(set())

print(seeds)
for i in range(len(maps)):
    print(maps[i])

total=0
results={}
ranges=set()
for i in range(0,len(seeds)-1,2):
    bottom=seeds[i]
    top=seeds[i+1]+bottom
    ranges.add((bottom,bottom,seeds[i+1]))
    total+=top
print(total)
print(ranges)

#This logic is broken, I need to keep track of how each range maps to the next layer, so I can follow back from the lowest location range to a seed.
#This should also probably be global? I can start with all the starting ranges, and build out from there
# for each mapping layer:
# take the current list of ranges and push to a heap (seed,mapped,range?)
# while the heap has entries:
# pop a range, check against the map, break it down when it overlaps a map boundary. add processed ranges to a temp set of ranges (as (seed,mapped,range) tuple), and unprocessed to the heap
# finish by copying the temp set to the set of ranges

for maplayer in maps:
    heap=deque()
    tempranges=set()
    for r in ranges:
        heap.append(r)
    while len(heap>0):
        s,b,o = heap.popleft()
        for l,h,offset in xmap:
            if l <= b <= h:
                if b+o <= h:
                    nb=b+offset
                    tempranges.add((s,nb,o))
                elif t > h:
                    nb=b+offset
                    no=h-l
                    tempranges.add((s,nb,no))
                    nb=h+1
                    no=o-(h-l)
                    heap.append((s,nb,no))
    ranges=set(tempranges)

#    for seed in range(bottom,top):
#        location=seed
#        for map in maps:
##            print(f'trying map {map} for {location}')
#            for mapping in map:
#                if mapping[0] <= location <= mapping[1]:
##                    print(f'found mapping for {location} in map {mapping}')
#                    location=location+mapping[2]
##                    print(f'new value: {location}')
#                    break
#        results[seed]=location
#print (f'{results[min(results, key=results.get)]}')
#
#
