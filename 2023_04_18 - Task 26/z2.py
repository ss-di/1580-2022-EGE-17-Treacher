with open('z2.txt') as f:
    data = f.readlines()
print(data)

n, dengi = map(int, data[0].split())
del data[0]
print(n, dengi, data)

A = []
B = []
for i in range(n):
    price, kol, t = data[i].split()
    price = int(price)
    kol = int(kol)
    if t == 'A':
        A.append((price, kol))
    else:
        B.append((price, kol))
        
print(A)
print(B)
A.sort()
B.sort()
for price, kol in A:
    if price*kol <= dengi:
        dengi -= price*kol
    else:
        kol = dengi // price
        dengi -= price*kol

print(dengi)

cnt = 0
for price, kol in B:
    if price*kol <= dengi:
        dengi -= price*kol
        cnt += kol
    else:
        kol = dengi // price
        dengi -= price*kol
        cnt += kol
print(cnt, dengi)
