with open("24_7094.txt") as f:
    s = f.readline()
    
print(len(s), s[:3], s[-3:])
s = s[:-1]
print(len(s), s[:3], s[-3:])

s = s.replace("U", "A")
s = s.replace("D", "C")
s = s.replace("F", "C")

p = "CA"
while p in s:
    p = p + "CA"
print((len(p)-2)//2)