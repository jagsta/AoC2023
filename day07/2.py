import sys

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

cards={}
for line in f.readlines():
    hand = line.rstrip("\n").split(" ")
    print(line,hand[0],hand[1])
    cards[hand[0]]=int(hand[1])

highs={}
pairs={}
twopairs={}
threes={}
houses={}
fours={}
fives={}

for hand,bid in cards.items():
    print(hand)
    this={}
    bump=0
    for card in hand:
        if card in this:
            this[card]+=1
        else:
            this[card]=1
    if "J" in this:
        bump=this["J"]
        this["J"]=0
    sets =list(reversed(sorted(this.values())))
    print(sets)
    if sets[0]+bump==5:
        fives[hand]=bid
    elif sets[0]+bump==4:
        fours[hand]=bid
    elif sets[0]+bump==3 and sets[1]==2:
        houses[hand]=bid
    elif sets[0]+bump==3:
        threes[hand]=bid
    elif sets[0]+bump==2 and sets[1]==2:
        twopairs[hand]=bid
    elif sets[0]+bump==2:
        pairs[hand]=bid
    else:
        highs[hand]=bid

def sortCA(arr):
    customAl='J23456789TQKA'
    dt = {c: i for i, c in enumerate(customAl)}
    return sorted(arr, key=lambda x: [dt[c] for c in x])

print(f'fives {sorted(fives)},fours {sorted(fours)},houses {sorted(houses)},threes {sorted(threes)},twopairs {sorted(twopairs)},pairs {sorted(pairs)},highs {sorted(highs)}')
rank=1
total=0
for card in sortCA(highs):
    total+=rank*highs[card]
    print(card,rank,highs[card],total)
    rank+=1
for card in sortCA(pairs):
    total+=rank*pairs[card]
    print(card,rank,pairs[card],total)
    rank+=1
for card in sortCA(twopairs):
    total+=rank*twopairs[card]
    print(card,rank,twopairs[card],total)
    rank+=1
for card in sortCA(threes):
    total+=rank*threes[card]
    print(card,rank,threes[card],total)
    rank+=1
for card in sortCA(houses):
    total+=rank*houses[card]
    print(card,rank,houses[card],total)
    rank+=1
for card in sortCA(fours):
    total+=rank*fours[card]
    print(card,rank,fours[card],total)
    rank+=1
for card in sortCA(fives):
    total+=rank*fives[card]
    print(card,rank,fives[card],total)
    rank+=1

print(total)
