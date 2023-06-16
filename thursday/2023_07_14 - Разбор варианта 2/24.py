def calc_digit(s):
    digs = set()
    for c in s:
        if '0' <= c <= '9':
            digs.add(c)
    return len(digs)

with open("24.txt") as f:
    data = f.readline()
    
print(data[:2], data[-2:])

v = data.split("SOLO")
print(len(v))

#d = []
#for w in v:
#    d.append(calc_digit(w))
    
#print(len(d), d[:2], d[-2:], sum(d))

mx_s = ""
for i in range(len(v)-4):
    s = "SOLO".join(v[i:i+5])
    cnt_d = calc_digit(s)
    if cnt_d >= 5 and len(s) > len(mx_s):
        mx_s = s
        p = i

print(len(mx_s), p)