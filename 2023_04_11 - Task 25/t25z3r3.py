'''
01234567
1?2139*4
'''

import fnmatch

for x in range(2023, 10**10+1, 2023):
    sx = str(x)
    if fnmatch.fnmatch(sx, '1?2139*4'):
        print(x, x // 2023)
