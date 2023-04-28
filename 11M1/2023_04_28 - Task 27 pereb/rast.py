fn = '27-75.txt'
fn = '27-75a.txt'
fn = '27-75b.txt'
with open(fn) as f:
	data = f.readlines()
	
print(data[:2], data[-2:])

data = list(map(int, data))
print(data[:2], data[-2:])

n = data[0]
del data[0]
print(n, data[:2], data[-2:])

mins = 10**1000
for i in range(n):
	for j in range(i+3, n):
		s = data[i] + data[j]
		if s % 10 == 4 and s < mins:
			mins = s
			
if mins == 10**1000:
	mins = -1
print(mins)
