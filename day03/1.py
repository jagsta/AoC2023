import re

def adj(c1, c2, r, lol):
	adjacent=0
	cols = len(lol[0])-1
	rows = len(lol)
	colstart = int(c1)-1 if c1>0 else int(c1)
	colend = int(c2)+1 if c2<(cols-1) else int(c2)
	rowstart = r-1 if r>0 else r
	rowend = r+1 if r<(rows-1) else r
#	print (cols,rows,colstart,colend,rowstart,rowend)
	for i in range(rowstart,rowend+1):
		for j in range(colstart,colend+1):
			#print (i,j,lol[i][j])
			if not re.match(r'[0-9\.]',lol[i][j]):
				print ("symbol?", lol[i][j])
				adjacent=1
	return(adjacent)
			

schema=[]
row=0
total=0
with open('input') as f:
	for line in f:
		schema.append(line)
print (schema)
for list in schema:
	nums = re.finditer(r'(\d+)',list)
	for num in nums:
		adjacency = adj(num.start(),num.end()-1,row,schema)		
		print(num.group(), num.start(), num.end()-1, row, adjacency, total) 
		if adjacency:
			total += int(num.group())
	row +=1
print (total)
