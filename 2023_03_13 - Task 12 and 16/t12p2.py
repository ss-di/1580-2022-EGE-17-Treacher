s = '0'+'1'*15+'3'*26+'0'

while '00' not in s:
    s = s.replace('01', '220', 1)
    s = s.replace('02', '3201', 1)
    s = s.replace('03', '2012', 1)
        
print(s)
print(1, s.count('1'))
print(2, s.count('2'))
print(3, s.count('3'))