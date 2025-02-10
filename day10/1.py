import sys

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
        elif c!=".":
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
