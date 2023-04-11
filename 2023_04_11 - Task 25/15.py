import fnmatch
#01234567
#12*45*

for x in range(51, 10**6+1, 51):
    if fnmatch.fnmatch(str(x), "12*45*"):
        print(x, x//51)