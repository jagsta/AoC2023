import sys

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

hgrids=[]
hgrids.append([])
i=0
for line in f.readlines():
    if line.strip()=="":
        hgrids.append([])
        i+=1
    else:
        hgrids[i].append(line.strip())

for grid in hgrids:
    for row in grid:
        print(row)
    print()

vgrids=[]
i=0
for grid in hgrids:
    vgrids.append([])
    for j in range(len(grid[0])):
        line=""
        for k in range(len(grid)):
            line+=grid[k][j]
        vgrids[i].append(line)
    i+=1

for grid in vgrids:
    for col in grid:
        print(col)
    print()

def reflect(grids):
    total=0
    for grid in grids:
        isMirrored=False
        print(f'testing for symmetry')
        for a in range(len(grid)-1):
            if grid[a]==grid[a+1]:
                print(f'found symmetry at {a} and {a+1}, testing outwards. Grid is {len(grid)} wide')
                isMirrored=True
                for b in range(1,a+1,1):
                    if a+1+b<len(grid) and grid[a-b]!=grid[a+1+b]:
                        isMirrored=False
                    else:
                        print(f'and at {a-b} and {a+b+1}')
                if isMirrored:
                    print(f'adding {a+1}')
                    total+=(a+1)
    return total

total=0
print(f'trying horizontal symmetries')
total+=100*reflect(hgrids)
print(f'trying vertical symmetries')
total+=reflect(vgrids)

print(total)




