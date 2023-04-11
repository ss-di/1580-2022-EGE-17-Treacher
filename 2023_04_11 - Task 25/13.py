import fnmatch
#01234567
#123*567?

for x in range(169, 10**9+1, 169):
    if fnmatch.fnmatch(str(x), "123*567?"):
        print(x, x//169)