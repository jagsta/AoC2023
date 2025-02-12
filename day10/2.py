import sys
from collections import deque

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f = open(file)

def get_dirs(c):
    dirs=[]
    if c=="-":
        dirs=[(-1,0),(1,0)]
    elif c=="J":
        dirs=[(-1,0),(0,-1)]
    elif c=="F":
        dirs=[(0,1),(1,0)]
    elif c=="|":
        dirs=[(0,-1),(0,1)]
    elif c=="7":
        dirs=[(0,1),(-1,0)]
    elif c=="L":
        dirs=[(0,-1),(1,0)]
    return dirs


visited=set()
y=0
x=0
origin=None
grid={}
for line in f.readlines():
    for c in line.strip():
        if (x,y) not in grid:
            grid[(x,y)]={}
            grid[(x,y)]["next"]=set()
        if c=="S":
            origin=(x,y)
            c="L"
        adj=get_dirs(c)
        grid[(x,y)]["c"]=c
        for dx,dy in adj:
            grid[(x,y)]["next"].add((x+dx,y+dy))
        x+=1
    y+=1
    maxx=x
    x=0
maxy=y
for y in range(maxy):
    s=""
    for x in range(maxx):
        s+=grid[(x,y)]["c"]
    print(s)

print(origin)
print(grid)

count=1
met=False
n=[]
visited.add(origin)
for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
    for x,y in get_dirs(grid[(origin[0]+dx,origin[1]+dy)]["c"]):
        if x+dx==0 and y+dy==0:
            n.append((origin[0]+dx,origin[1]+dy))
            visited.add((origin[0]+dx,origin[1]+dy))
print(n)
print(visited)
while not met:
    nstep=[]
    for step in n:
        for nn in grid[step]["next"]:
            if nn not in visited:
                nstep.append(nn)
                visited.add(nn)
                print(f'from:{step} to {nn}')
    n=nstep.copy()
    if len(n)==0:
        break
    count+=1

print(count)
spaces={}
for coord in grid:
    if coord not in visited:
        spaces[coord]="."

for y in range(maxy):
    s=""
    for x in range(maxx):
        if (x,y) in spaces:
            s+=spaces[(x,y)]
        else: s+=grid[(x,y)]["c"]
    print(s)

for y in range(maxy):
    s=""
    for x in range(maxx):
        if (x,y) in spaces:
            s+=spaces[(x,y)]
        else: s+=" "
    print(s)




triplegrid={}
for y in range(maxy):
    for x in range(maxx):
        if (x,y) in spaces:
            for nx,ny in [(3*x,3*y),(3*x+1,3*y),(3*x+2,3*y),(3*x,3*y+1),(3*x+2,3*y+1),(3*x,3*y+2),(3*x+1,3*y+2),(3*x+2,3*y+2)]:
                triplegrid[(nx,ny)]=" "
            triplegrid[(3*x+1,3*y+1)]="."
        else:
            for nx,ny in [(3*x,3*y),(3*x+1,3*y),(3*x+2,3*y),(3*x,3*y+1),(3*x+2,3*y+1),(3*x,3*y+2),(3*x+1,3*y+2),(3*x+2,3*y+2)]:
                triplegrid[(nx,ny)]=" "
            c=grid[(x,y)]["c"]
            triplegrid[(3*x+1,3*y+1)]=c
            if c=="F":
                triplegrid[(3*x+2,3*y+1)]=c
                triplegrid[(3*x+1,3*y+2)]=c
            elif c=="7":
                triplegrid[(3*x,3*y+1)]=c
                triplegrid[(3*x+1,3*y+2)]=c
            elif c=="L":
                triplegrid[(3*x+2,3*y+1)]=c
                triplegrid[(3*x+1,3*y)]=c
            elif c=="J":
                triplegrid[(3*x,3*y+1)]=c
                triplegrid[(3*x+1,3*y)]=c
            elif c=="|":
                triplegrid[(3*x+1,3*y+2)]=c
                triplegrid[(3*x+1,3*y)]=c
            elif c=="-":
                triplegrid[(3*x,3*y+1)]=c
                triplegrid[(3*x+2,3*y+1)]=c

for y in range(3*maxy):
    s=""
    for x in range(3*maxx):
       s+=triplegrid[(x,y)]
    print(s)



beenthere=set()
for start in [(0,0),(0,3*maxy),(3*maxx,3*maxy),(3*maxx,0)]:
    heap=deque()
    heap.append(start)
    while len(heap)>0:
        x,y=heap.popleft()
        beenthere.add((x,y))
        if (x,y) in triplegrid and triplegrid[(x,y)]==".":
            spaces[((x-1)//3,(y-1)//3)]="O"
        for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            if (x+dx,y+dy) in triplegrid and (triplegrid[(x+dx,y+dy)]==" " or triplegrid[(x+dx,y+dy)]=="."):
                if (x+dx,y+dy) not in beenthere:
                    beenthere.add((x+dx,y+dy))
                    heap.append((x+dx,y+dy))


inside=0
for y in range(maxy):
    s=""
    for x in range(maxx):
        if (x,y) in spaces:
            s+=spaces[(x,y)]
            if spaces[(x,y)]!="O":
                inside+=1
        else:
           # s+=grid[(x,y)]["c"]
           s+=" "

    print(s)

print(inside)
