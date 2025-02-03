with open('input') as f:
	total=0
	for line in f:
		first = ''
		second = ''
		for i in line:
			if i.isnumeric():
				if first:
					second = i
				else:
					first = i
		#print (first, second)
		if not second:
			second = first
		#print (first, second)
		num = first + second
		if num.isnumeric():
			total = total + int(num)
			print (first, second, num, total)
print (total)
