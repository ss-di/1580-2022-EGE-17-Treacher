import itertools

s = 'РУСЛАН'

#p = list(itertools.product(s, repeat=6))
p = list(itertools.permutations(s))

print(len(p))
cnt = 0
for i in p:
    s = ''.join(i)
    if not ('УА' in s) and not ('АУ' in s):
        cnt += 1
        print(s)
print(cnt)