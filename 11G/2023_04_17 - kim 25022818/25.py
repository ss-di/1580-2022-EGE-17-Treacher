import fnmatch

for i in range(129, 10**8+1, 129):
    if fnmatch.fnmatch(str(i), '12?3*46'):
        print(i, i // 129)
        
for i in range(129*2, 10**8+1, 129):
    s = str(i)
    if s[:2] == '12' and \
       s[3] == '3' and \
       s[-2:] == '46':
        print(i, i // 129)        
