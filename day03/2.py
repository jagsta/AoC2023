import re
import sys

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

def adj(c1, c2, r, lol):
    global stars
    adjacent=False
    cols = len(lol[0])
    rows = len(lol)
    colstart = int(c1)-1 if c1>0 else int(c1)
    colend = int(c2)+1 if c2<(cols-1) else int(c2)
    rowstart = r-1 if r>0 else r
    rowend = r+1 if r<(rows-1) else r
#	print (cols,rows,colstart,colend,rowstart,rowend)
    for i in range(rowstart,rowend+1):
        for j in range(colstart,colend+1):
            #print (i,j,lol[i][j])
            if lol[i][j]=="*":
                stars+=1
                print ("symbol?",i,j, lol[i][j])
                if (i,j) not in adjacencies:
                    adjacencies[(i,j)]=set()
                adjacent=(i,j)
    return adjacent

adjacencies={}
schema=[]
row=0
total=0
stars=0
with open(file) as f:
	for line in f:
		schema.append(line)
print (schema)
for list in schema:
    nums = re.finditer(r'(\d+)',list)
    for num in nums:
        adjacency = adj(num.start(),num.end()-1,row,schema)
        print(num.group(), num.start(), num.end()-1, row, adjacency, total)
        if adjacency:
            if int(num.group()) in adjacencies[adjacency]:
                print(f'dupe number for {adjacency}:{num.group()}')
                adjacencies[adjacency].add(int(num.group())**2)
                adjacencies[adjacency].remove(int(num.group()))
                adjacencies[adjacency].add(1)
            else:
                adjacencies[adjacency].add(int(num.group()))
    row +=1

for coord,star in adjacencies.items():
    print(f'{coord} has {star}')

count=0
for gears in adjacencies.values():
    if len(gears)==2:
        count+=1
        product=1
        for x in gears:
            product*=x
#            print(f'product for {x} is {product}')
        total+=product
#        print(f'total is {total}')

print(total)
print(stars)
print(len(adjacencies))
print(count)
