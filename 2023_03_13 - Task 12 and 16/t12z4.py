def f(s):
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)
    return s

for i in range(61, 100):
    s = f('1'*i)
    if s == '221':
        print(i)

#print(s)
#print(1, s.count('1'))
#print(2, s.count('2'))