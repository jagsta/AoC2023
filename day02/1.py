import re
with open('input') as f:
	power=0
	total=0
	rmax=12
	bmax=14
	gmax=13
	for line in f:
		game= re.search(r'Game (\d+):', line)
		id=game.group(1)
		words= re.findall(r'(\d+) (blue|green|red)', line)
		#matches= re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
		#words = [match.group(1) for match in matches]
		#print (words)
		impossible=0
		minr=0
		minb=0
		ming=0
		for tuple in words:
			if tuple[1] == "red":
				if int(tuple[0])>minr:
					minr=int(tuple[0])
				if int(tuple[0])>rmax:
					print (tuple, "red too high")
					impossible=1
			elif tuple[1] == "blue":
				if int(tuple[0])>minb:
					minb=int(tuple[0])
				if int(tuple[0])>bmax:
					print (tuple, "blue too high")
					impossible=1
			elif tuple[1] == "green":
				if int(tuple[0])>ming:
					ming=int(tuple[0])
				if int(tuple[0])>gmax:
					print (tuple, "green too high")
					impossible=1
		if not impossible:
			total = total + int(id)
		power = power + (minr * ming * minb)
		#first = words[0]
		#second = words[-1]
		#first=tonum(first)
		#second=tonum(second)
		#num = first + second
		#first = ''
		#second = ''
		#for i in line:
		#	if i.isnumeric():
		#		if first:
		#			second = i
		#		else:
		#			first = i
		#print (first, second)
		#	total = total + int(num)
		#	print (first, second, num, total)
print ("total", total)
print ("power", power)
