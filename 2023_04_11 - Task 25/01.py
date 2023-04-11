def is_prime(x):
    if x == 1:
        return False
    d = 2
    while d*d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

A = 3532000
B = 3532160

cnt = 0
for x in range(A, B+1):
    if is_prime(x):
        cnt += 1
        print(cnt, x)