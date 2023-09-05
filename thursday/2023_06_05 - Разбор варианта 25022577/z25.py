import fnmatch

for x in range(21, 10**8 + 1, 21):
    if fnmatch.fnmatch(str(x), "1234*54"):
        print(x, x // 21)