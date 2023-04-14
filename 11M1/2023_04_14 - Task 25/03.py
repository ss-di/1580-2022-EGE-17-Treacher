#01234567
#1?2139*4

import fnmatch

for i in range(2023, 10**10+1, 2023):
    s = str(i)
    if fnmatch.fnmatch(s, '1*2139*4'):
        print(i, i // 2023)