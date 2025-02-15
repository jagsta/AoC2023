import sys
import re
from itertools import combinations
from itertools import permutations
from itertools import product


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

li=["#","."]
total=0
for line in lines:
    line["string"]=line["string"]+"?"+line["string"]+"?"+line["string"]+"?"+line["string"]+"?"+line["string"]
    line["blocks"]=[*line["blocks"],*line["blocks"],*line["blocks"],*line["blocks"],*line["blocks"]]
    print(line["string"],line["blocks"])
    matches=0
    length=(line["blanks"]*5)+4
    hashes=line["string"].count("#")
    tothashes=sum(line["blocks"])
    missing=tothashes-hashes
    print(li)
    candidates=[''.join(comb) for comb in product(li, repeat=length) if comb.count("#")==missing]
    print(len(candidates))
    #print(candidates)
    string="(^\.*"
    for num in line["blocks"]:
        string+='#{'+str(num)+'}'+'\.+'
    string=string[:-3]+"\.*$)"
    print(line,string)
    for cand in candidates:
        perm=""
        i=0
        for c in line["string"]:
            if c=="?":
                perm+=cand[i]
                i+=1
            else:
                perm+=c
        match=re.search(string,perm)
        if match:
            matches+=1
            print(perm,match.group(0))
#        else:
#            print(perm)
    print(matches)
    total+=matches
print(total)
