import sys
from itertools import combinations

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)


y=0
x=0
grid={}
for line in f.readlines():
    for c in line.rstrip("\n"):
        print(c)
        grid[(x,y)]=c
        x+=1
    xmax=x
    x=0
    y+=1
ymax=y

for y in range(ymax):
    s=""
    for x in range(xmax):
        s+=grid[(x,y)]
    print(s)

for y in range(ymax-1,-1,-1):
    galaxies=False
    for x in range(xmax):
        if grid[(x,y)]=="#":
            galaxies=True
    if galaxies==False:
        for yz in range(ymax-1,y-1,-1):
            for xz in range(xmax):
                grid[(xz,yz+1)]=grid[(xz,yz)]
                print(f'copying {xz,yz} to {xz,yz+1}')
        ymax+=1
print(xmax, ymax)
for x in range(xmax-1,-1,-1):
    galaxies=False
    for y in range(ymax):
        if grid[(x,y)]=="#":
            galaxies=True
    if galaxies==False:
        for xz in range(xmax-1,x-1,-1):
            for yz in range(ymax):
                grid[(xz+1,yz)]=grid[(xz,yz)]
                print(f'copying {xz,yz} to {xz+1,yz}')
        xmax+=1

for y in range(ymax):
    s=""
    for x in range(xmax):
        s+=grid[(x,y)]
    print(s)

galaxies=[]
for coord,v in grid.items():
    if v=="#":
        galaxies.append(coord)
perm = combinations(galaxies,2)
distance=0
for i in list(perm):
    distance+=abs(i[0][0]-i[1][0])+abs(i[0][1]-i[1][1])
    print(i)

print(distance)
