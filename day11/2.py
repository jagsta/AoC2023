import sys
from itertools import combinations

file="input.txt"
expansion=1
if len(sys.argv)>1:
    file=sys.argv[1]

if len(sys.argv)>2:
    expansion=int(sys.argv[2])

f=open(file)


y=0
x=0
grid={}
gals=set()
for line in f.readlines():
    for c in line.rstrip("\n"):
        grid[(x,y)]={}
        grid[(x,y)]["c"]=c
        grid[(x,y)]["cost"]=1
        if c=="#":
            gals.add((x,y))
        x+=1
    xmax=x
    x=0
    y+=1
ymax=y

for y in range(ymax):
    s=""
    for x in range(xmax):
        s+=grid[(x,y)]["c"]
    print(s)

for y in range(ymax):
    galaxies=False
    for x in range(xmax):
        if grid[(x,y)]["c"]=="#":
            galaxies=True
    if galaxies==False:
        for xz in range(xmax):
            grid[(xz,y)]["cost"]=expansion

for x in range(xmax):
    galaxies=False
    for y in range(ymax):
        if grid[(x,y)]["c"]=="#":
            galaxies=True
    if galaxies==False:
        for yz in range(ymax):
            grid[(x,yz)]["cost"]=expansion

perm = combinations(gals,2)
distance=0
for i in list(perm):
    last=distance
    if i[0][0]>i[1][0]:
        xstart=i[1][0]
        xend=i[0][0]
        ycol=i[0][1]
    else:
        xstart=i[0][0]
        xend=i[1][0]
        ycol=i[1][1]
    if i[0][1]>i[1][1]:
        ystart=i[1][1]
        yend=i[0][1]
        xcol=i[1][0]
    else:
        ystart=i[0][1]
        yend=i[1][1]
        xcol=i[0][0]
    for x in range(xstart,xend):
        distance+=grid[(x,ycol)]["cost"]
    for y in range(ystart,yend):
        distance+=grid[(xcol,y)]["cost"]

print(distance)
