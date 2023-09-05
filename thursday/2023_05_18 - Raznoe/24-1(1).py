with open('24-1(1).txt') as f:
    data = f.readline()

print(data[:3], data[-3:])
print(1)
#data = data[:-1]
data = data.strip()
print(data[:3], data[-3:])
print(1)

p = data.split("A")
print(p[:5])
# k1 A k2 A k3 A k4 A k5 A k6 k7

mx_len = 0
for i in range(len(p)-5):
    part = p[i:i+6]
    cnt_d = part[0].count("D") + \
            part[1].count("D") + \
            part[2].count("D") + \
            part[3].count("D") + \
            part[4].count("D") + \
            part[5].count("D")
    pl = len(part[0]) + \
         len(part[1]) + \
         len(part[2]) + \
         len(part[3]) + \
         len(part[4]) + \
         len(part[5]) + 5
    if  cnt_d >= 20 and pl > mx_len:
        mx_len = pl
        
print(mx_len)