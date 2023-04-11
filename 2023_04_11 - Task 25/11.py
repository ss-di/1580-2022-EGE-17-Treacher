#01234567
#1?2139*4
# r1   r2
ans = []
for r1 in range(10):
    r2 = ''
    x = 0
    while x <= 10**10:
        x = int(f"1{r1}2139{r2}4")
        if x % 2023 == 0:
            ans.append((x, x // 2023))
        if r2 == '':
            r2 = 0
        else:
            r2 += 1
ans.sort()
print(*ans, sep='\n')