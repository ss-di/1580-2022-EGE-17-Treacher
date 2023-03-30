f=open('17.txt')
l=f.readlines()
print(l)
cnt=0
mxsum=0
mx12=0
for i in range(0,len(l)):
    l[i] = l[i][:-1]
    if l[i][len(l[i])-2:]== '12':
        if int(l[i]) > mx12:
            mx12 = int(l[i])
print(mx12)
for i in range(0,len(l)-1):
    a=0
    b=0
    if l[i][len(l[i])-2:]== '12':
        a=int(l[i])
    if l[i+1][len(l[i+1])-2:]== '12':
        b=int(l[i+1])
    print(a,b)
    if (a != 0  and b == 0) or (a == 0  and b != 0):
        if (int(l[i])+int(l[i+1]))**2 < (mx12)**2:
            cnt+=1
            if (int(l[i])+int(l[i+1])) > mxsum:
                mxsum = (int(l[i])+int(l[i+1]))
print(cnt, mxsum, 3)
