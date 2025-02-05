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

results={}
for seed in seeds:
    location=seed
    for map in maps:
  #      print(f'trying map {map} for {location}')
        for mapping in map:
            if mapping[0] <= location <= mapping[1]:
                #print(f'found mapping for {location} in map {mapping}')
                location=location+mapping[2]
                #print(f'new value: {location}')
                break
    results[seed]=location
    print (f'{dict(sorted(results.items(), key=lambda item: item[1]))}')


