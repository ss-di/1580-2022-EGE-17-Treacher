#01234567
#1?2139*4

for i in range(1, 10**10+1):
    s = str(i)
    if i % 2023 == 0 and \
       s[0] == '1' and \
       s[2:2+4] == '2139' and \
       s[-1] == '4':
        print(i, i // 2023)