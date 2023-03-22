m = list(map(int, open('zz17-1.txt').readlines()))

lm = []
for i in range(1, len(m)-1):
    if m[i-1] < m[i] > m[i+1]:
        lm.append(i)

mn = len(lm)
for i in range(len(lm)-1):
    mn = min(mn, lm[i+1] - lm[i])
    
print(len(lm), mn)