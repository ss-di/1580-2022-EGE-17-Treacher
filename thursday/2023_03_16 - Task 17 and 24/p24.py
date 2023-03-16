s = open('24-250.txt').readline()

print(len(s))

dots = []
for i in range(len(s)):
    if s[i] == '.':
        dots.append(i)
        
print(dots[:10])

mn = dots[6]-dots[0]+1
for i in range(len(dots)-7 + 1):
    mn = min(mn, dots[i+6]-dots[i]+1)
print(mn)
    