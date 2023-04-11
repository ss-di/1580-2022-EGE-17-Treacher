# 0123456789
#'aaaABdfdBA'
#    1234567


def work(s):
    cnt = mx = 0
    while True:
        pAB = s.find('AB')
        pBA = s.find('BA')
        if pAB == -1 or pBA == -1:
            return cnt, mx
        if pBA < pAB:
            s = s[pBA + 1:]
            continue
        s1 = s[pAB:pBA+2]
        if s1.count('A') > 2 or s1.count('B') > 2:
            s = s[pAB + 1:]
            continue
#        if len(s1) == 3:
#            s = s[pAB + 1:]
#            continue
        print(s1)
        cnt += 1
        mx = max(mx, len(s1))
        s = s[pAB + 1:]

data = open('39618-1.txt').readlines()
#data = open('24-k-1.txt').readlines()

print(len(data))

cnt = mx = 0
for s in data:
    cnt1, mx1 = work(s)
    cnt += cnt1
    mx = max(mx, mx1)

print(cnt, mx)