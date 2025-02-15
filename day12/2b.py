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
    if line["string"][:line["blocks"][0]].count("#")==line["blocks"][0] or line["string"][-line["blocks"][-1]:].count("#")==line["blocks"][-1]:
        print("blocks adjacent to beginning or end")
        linea="."+line["string"]
        lineb=line["string"]+"."
    else:
        linea="?"+line["string"]
        lineb=line["string"]+"?"
    lineablocks=line["blocks"].copy()
    linebblocks=line["blocks"].copy()
    # Test line a and b
    candidatesab=[''.join(comb) for comb in product(li, repeat=line["blanks"]+1) if comb.count("#")==sum(lineablocks)-linea.count("#")]
    candidates=[''.join(comb) for comb in product(li, repeat=(line["blanks"])) if comb.count("#")==sum(line["blocks"])-line["string"].count("#")]
    print(line["string"],line["blocks"])
    stringa="(^\.*"
    for num in lineablocks:
        stringa+='#{'+str(num)+'}'+'\.+'
    stringa=stringa[:-3]+"\.*$)"
    stringb="(^\.*"
    for num in linebblocks:
        stringb+='#{'+str(num)+'}'+'\.+'
    stringb=stringb[:-3]+"\.*$)"
    string="(^\.*"
    for num in line["blocks"]:
        string+='#{'+str(num)+'}'+'\.+'
    string=string[:-3]+"\.*$)"
    matchesa=0
    for cand in candidatesab:
        perm=""
        i=0
        for c in linea:
            if c=="?":
                perm+=cand[i]
                i+=1
            else:
                perm+=c
        match=re.search(stringa,perm)
        if match:
            matchesa+=1
            print(perm,match.group(0))
#        else:
#            print(perm)
    print(f'a {matchesa}')
    matchesb=0
    for cand in candidatesab:
        perm=""
        i=0
        for c in lineb:
            if c=="?":
                perm+=cand[i]
                i+=1
            else:
                perm+=c
        match=re.search(stringb,perm)
        if match:
            matchesb+=1
            print(perm,match.group(0))
#        else:
#            print(perm)
    print(f'b {matchesb}')
    matchesd=0
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
            matchesd+=1
            print(perm,match.group(0))
#        else:
#            print(perm)
    print(f'd {matchesd}')

    if matchesa>matchesb:
        matches=(matchesa**4)*matchesd
    elif matchesb>matchesa:
        matches=(matchesb**4)*matchesd
    else:
        matches=matchesd**5
    print(matches)
    total+=matches
print(total)
