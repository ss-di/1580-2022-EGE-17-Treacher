s = open("24-153.txt").readline()

print(1, s[:5]) # copy(s, p, len) s[p:p+len]
print(2, s[-3:])
s = s[:-1]
print(3, s[-3:])

print('EABEABE' in s)
print('EABEABEA' in s)

#s='EBCEABEABEBECBCACE'
#p = s.find('EABEABE')
#print(s[p-3:p+15])

p = '*'
cur = mx = 0
for i in range(len(s)):
    if (p != 'E' and cur == 0 or p == 'B') and s[i] == 'E' or \
       p == 'E' and s[i] == 'A' or \
       p == 'A' and s[i] == 'B':
        cur += 1
        mx = max(mx, cur)
        if cur == 8:
            print(s[i-7:i+1])
    else:
        if s[i] == 'E':
            cur = 1
        else:
            cur = 0
    p = s[i]
    
print(1, mx)

frag = 'E'
for i in range(1, len(s)+2):
    if frag in s:
        print(i, frag)
        frag = frag + 'EAB'[i%3]
    else:
        break