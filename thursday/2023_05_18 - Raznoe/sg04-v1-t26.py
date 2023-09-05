with open('26.txt') as f:
    data = f.readlines()
    
n = int(data[0])
del data[0]

for i in range(n):
    a, b, c = data[i].split()
    data[i] = [int(a), int(b), c]

data.sort()
print(data)

pA = [0] * 80
pB = [0] * 20

cntA = 0
cntF = 0

for i in range(n):
    p, d, t = data[i]
    if t=='A':
        for j in range(80):
            if pA[j] <= p:
                cntA += 1
                pA[j] = p+d
                break
        else:
            for j in range(20):
                if pB[j] <= p:
                    cntA += 1
                    pB[j] = p+d
                    break
            else:
                cntF += 1
    else:
        for j in range(20):
            if pB[j] <= p:
                pB[j] = p+d
                break
        else:
            cntF += 1

print(cntA, cntF)        