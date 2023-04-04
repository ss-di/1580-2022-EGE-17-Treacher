s = open("z6.txt").readline()

print(1, s[:5]) # copy(s, p, len) s[p:p+len]
print(2, s[-3:])
#s = s[:-1]
#print(3, s[-3:])

cnt = [0] * 26
for i in range(1, len(s)):
    if s[i-1] == 'A':
        cnt[ord(s[i]) - ord('A')] += 1

print(cnt)
mx = max(cnt)
print(mx)
imx = cnt.index(mx)
print(imx)
print(chr(ord('A') + imx))

s2 = ''
for i in range(1, len(s)):
    if s[i-1] == 'A':
        s2 += s[i]

alf = 'QWERTYTUIOPASDFGHJKLZXCVBNM'
cnt2 = []
for c in alf:
    print(c, s2.count(c))
    cnt2.append((s2.count(c), c))
print(max(cnt2))
