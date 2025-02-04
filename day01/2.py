import re

def tonum(word):
	if word == 'one':word = '1'
	if word == 'two':word = '2' 
	if word == 'three':word = '3' 
	if word == 'four':word = '4' 
	if word == 'five':word = '5' 
	if word == 'six':word = '6' 
	if word == 'seven':word = '7' 
	if word == 'eight':word = '8' 
	if word == 'nine':word = '9' 
	return(word)

with open('input') as f:
	total=0
	for line in f:
		#words= re.findall("\d|one|two|three|four|five|six|seven|eight|nine", line)
		matches= re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
		words = [match.group(1) for match in matches]
		print (words)
		first = words[0]
		second = words[-1]
		first=tonum(first)
		second=tonum(second)
		num = first + second
		if num.isnumeric():
			total = total + int(num)
			print (line, words, first,second,num,total)
print (total)
