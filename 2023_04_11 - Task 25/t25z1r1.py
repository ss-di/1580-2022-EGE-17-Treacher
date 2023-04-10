def is_prime(x):
    cnt = 0
    for d in range(1, x+1):
        if x % d == 0:
            cnt += 1
    return cnt == 2


A = 3532000
B = 3532160
cnt = 0
for x in range(A, B+1):
    if is_prime(x):
        cnt += 1
        print(cnt, x)
