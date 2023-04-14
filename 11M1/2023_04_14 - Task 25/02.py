#01234567
#1?2139*4
# r1   r2

for r1 in range(10):
    x = int(f'1{r1}21394') # x = int('1' + str(r1) + '2139' + str(r2) + '4')
    if x % 2023 == 0:
        print(x, x // 2023)

for r1 in range(10):
    x = int(f'1{r1}213904') # x = int('1' + str(r1) + '2139' + str(r2) + '4')
    if x % 2023 == 0:
        print(x, x // 2023)

d2 = 1
x = 0
while x <= 10**10:
    for r2 in range(10**(d2-1), 10**d2 ):
        print(r2)
        for r1 in range(10):
            x = int(f'1{r1}2139{r2}4') # x = int('1' + str(r1) + '2139' + str(r2) + '4')
            if x % 2023 == 0:
                print(x, x // 2023)
    d2 += 1
