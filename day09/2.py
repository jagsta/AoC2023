import sys

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f=open(file)

def get_next(seq):
    deltas=[seq]
    deltas.append([])
    layer=1
    found=False
    while not found:
        for i,num in enumerate(deltas[layer-1][:-1]):
            deltas[layer].append(deltas[layer-1][i+1]-num)
        if sum(deltas[layer])==0:
            found=True
        else:
            deltas.append([])
            layer+=1
    result=0
    last=0
    print(len(deltas))
    for i in range(len(deltas)-1,0,-1):
        target=deltas[i-1][0]
        result=target-last
        last=result
        print(i,result,deltas[i])
    return result



total=0
for line in f.readlines():
    sequence= [int(i) for i in line.rstrip("\n").split()]
    total+=get_next(sequence)

print(total)

