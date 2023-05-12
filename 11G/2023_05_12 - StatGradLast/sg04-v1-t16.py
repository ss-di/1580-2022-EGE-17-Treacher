'''
F(n) = n, если n > 1 000 000;
F(n) = n + F(2n), если n ≤ 1 000 000;
G(n) = F(n) / n.
'''

def F(n):
    if n > 1_000_000:
        return n
    return n + F(2*n)

def G(n):
    return  F(n) / n

a = G(1000)

cnt = 0
for i in range(1, 100000):
    if G(i) == a:
        cnt += 1

print(cnt)