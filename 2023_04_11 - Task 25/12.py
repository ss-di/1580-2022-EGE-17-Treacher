#01234567
#123*567?
# r1   r2
ans = []
for r1 in range(10):
    r2 = ''
    x = 0
    while x <= 10**9:
        x = int(f"123{r2}567{r1}")
        if x % 169 == 0:
            ans.append((x, x // 169))
        if r2 == '':
            r2 = 0
        else:
            r2 += 1
ans.sort()
print(*ans, sep='\n')