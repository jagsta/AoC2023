import sys

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]


total=0
with open(file) as f:
    for line in f.readlines():
        print(line)
        thisscore=0
        winners=set()
        numbers=set()
        halves=line.strip().split("|")
        wins=halves[0].split()
        for win in wins[2].split(","):
            print (win)
            if win.isdigit():
                print(f'winning number: {win}')
                winners.add(int(win))
        nums=halves[1].split(",")
        for num in nums:
            print(num)
            if num.isdigit():
                print(f'adding number: {num}')
                numbers.add(int(num))
        for win in winners:
            if win in numbers:
                if thisscore==0:
                    thisscore+=1
                else:
                    thisscore*=2
                print(f'winning number: {win} in numbers, this score is: {thisscore}')
        total+=thisscore
print(total)
