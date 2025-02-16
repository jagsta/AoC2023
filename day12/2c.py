import sys
import re
from itertools import combinations
from itertools import permutations
from itertools import product
from collections import deque


file="input.txt"
if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

lines=[]
l=0
for line in f.readlines():
    blanks=0
    lines.append({})
    lines[l]["string"]=""
    chunk = line.rstrip("\n").split()
    for c in chunk[0]:
        if c=="?":
            blanks+=1
        lines[l]["string"]+=c
    lines[l]["blanks"]=blanks
    lines[l]["blocks"]=[]
    for n in chunk[1].split(","):
        lines[l]["blocks"].append(int(n))
    l+=1

def rec(string,s,blocks,b):
    if (s,b) in cache:
        print(f'hit cache for {s},{b}: {cache[(s,b)]}')
        return cache[(s,b)]
    count=0
    if b==len(blocks) and string[s:].count("#")==0:
        print(f'Solution found')
        return 1
    if (s,b) in misses:
        return 0
    if b==0 and string[:s].count("#")>0:
        print(f'shifted past first block')
        return 0
    if sum(blocks[b:])+len(blocks)-b-1>len(string[s:]):
        misses.add((s,b))
        print(f'not enough string left:{s},{b} need {sum(blocks[b:])+len(blocks)-b-1}, got {len(string[s:])}')
        return 0
    if b<len(blocks):
        blocksize = blocks[b]
        if b==len(blocks)-1:
            matchstring="(?=(^[?#]{"+str(blocksize)+"})([.?]*$))"
        else:
            matchstring="(?=(^[?#]{"+str(blocksize)+"}[.?]))"
            #print(s,b,matchstring,string[s:])
        match=re.match(matchstring,string[s:])
        if match:
        #print(s,b,match.group(1),len(match.group(1)))
            if b==len(blocks)-1:
                count+=rec(string,s+blocksize+len(match.group(2)),blocks,b+1)
            else:
                count+=rec(string,s+blocksize+1,blocks,b+1)
        if string[s]!="#":
            count+=rec(string,s+1,blocks,b)
    else:
        misses.add(s,b)
        return 0
    cache[(s,b)]=count
    return count

def perm(string,strindex,blocks,blindex):
    count=0
    misses=set()
    heap=deque()
    heap.append((strindex,blindex))
    while len(heap)>0:
        s,b = heap.pop()
        if (s,b) in misses:
            continue
        if b==0 and string[:s].count("#")>0:
            print(f'shifted past first block')
            continue
        if sum(blocks[b:])+len(blocks)-b-1>len(string[s:]):
            misses.add((s,b))
            print(f'not enough string left:{s},{b} need {sum(blocks[b:])+len(blocks)-b-1}, got {len(string[s:])}')
            continue
        if b<len(blocks):
            blocksize = blocks[b]
            if b==len(blocks)-1:
                matchstring="(?=(^[?#]{"+str(blocksize)+"})([.?]*$))"
            else:
                matchstring="(?=(^[?#]{"+str(blocksize)+"}[.?]))"
            #print(s,b,matchstring,string[s:])
            match=re.match(matchstring,string[s:])
            if match:
                #print(s,b,match.group(1),len(match.group(1)))
                if b==len(blocks)-1:
                    heap.append((s+blocksize+len(match.group(2)),b+1))
                else:
                    heap.append((s+blocksize+1,b+1))
            if string[s]!="#":
                heap.append((s+1,b))
        elif string[s:].count("#")==0:
            count+=1
            #hits.add(st)
        else:
            #print(f'blocks left at end')
            misses.add((s,b))
            continue
    return count

total=0
for line in lines:
    misses=set()
    cache={}
    l=line["string"]+"?"+line["string"]+"?"+line["string"]+"?"+line["string"]+"?"+line["string"]
    lb=[*line["blocks"],*line["blocks"],*line["blocks"],*line["blocks"],*line["blocks"]]
    print(f'Trying {l} with blocks {lb}')
    count=rec(l,0,lb,0)
    total+=count
    print(count)
print(total)

