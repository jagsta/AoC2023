import sys
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
    ranges.add((bottom,top))
    total+=top
print(total)
print(ranges)

#This logic is broken, I need to keep track of how each range maps to the next layer, so I can follow back from the lowest location range to a seed.
#This should also probably be global? I can start with all the starting ranges, and build out from there
for bottom,top in ranges:
    xrange=set()
    xrange.add((bottom,top))
    print (bottom,top)
    for xmap in maps:
        rnext=set()
        redo=set()
        remove=set()
        for l,h,offset in xmap:
            for b,t in xrange:
                if l <= b <= h:
                    remove.add((b,t))
                    if t <= h:
                        nb=b+offset
                        nt=t+offset
                        rnext.add((nb,nt))
                    elif t > h:
                        nb=b+offset
                        nt=h+offset
                        rnext.add((nb,nt))
                        nb=h+1
                        nt=t
                        redo.add((nb,nt))
            xrange=xrange-remove
            xrange=xrange+redo
        xrange=rnext

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
