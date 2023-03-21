# 1
cnt = 0
mx = 0
for i in range(1016, 7937+1):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and \
        i % 19 != 0 and i % 27 != 0:
        cnt += 1
        mx = max(mx, i)
print(cnt, mx)

# 2
no = [7, 17, 19, 27]
a = list(filter(lambda x: x % 3 == 0 and all([x % d != 0 for d in no]), range(1016, 7937+1)))
print(len(a), max(a))
