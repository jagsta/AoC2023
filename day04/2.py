import sys

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]


cardcounts=[]
total=0
thiscard=0
with open(file) as f:
    for line in f.readlines():
        if thiscard >= len(cardcounts):
            cardcounts.append(1)
        else:
            cardcounts[thiscard]+=1
        thiscard+=1
        print(line)
        thisscore=0
        winners=set()
        numbers=set()
        halves=line.strip().split("|")
        wins=halves[0].split()
        for win in wins[2].split(","):
            #print (win)
            if win.isdigit():
                #print(f'winning number: {win}')
                winners.add(int(win))
        nums=halves[1].split(",")
        for num in nums:
            #print(num)
            if num.isdigit():
                #print(f'adding number: {num}')
                numbers.add(int(num))
        for win in winners:
            if win in numbers:
                thisscore+=1
        print(f'card {thiscard} score is: {thisscore}, we have {cardcounts[thiscard-1]} copies of this card')
        for _ in range(cardcounts[thiscard-1]):
            for i in range(thisscore):
                if 0 <= thiscard+i < len(cardcounts):
                    cardcounts[thiscard+i]+=1
                else:
                    cardcounts.append(1)
        print(cardcounts)
print(cardcounts)
for i in cardcounts:
    total+=i

print (total)
