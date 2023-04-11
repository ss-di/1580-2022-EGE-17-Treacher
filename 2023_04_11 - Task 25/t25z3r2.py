'''
01234567
1?2139*4
'''

x = 0
g = ''
while x <= 10**10:
    for r in range(10):
        x = int(f'1{r}2139{g}4')
        if x % 2023 == 0:
            print(x, x // 2023)
    if g == '':
        g = 0
    else:
        g += 1
