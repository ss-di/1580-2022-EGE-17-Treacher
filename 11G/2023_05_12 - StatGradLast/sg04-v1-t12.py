'''НАЧАЛО
ПОКА НЕ нашлось (00)
заменить (02, 101)
заменить (11, 2)
заменить (012, 30)
заменить (010, 00)
КОНЕЦ ПОКА
КОНЕЦ'''

def avt(s):
    while '00' not in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('012', '30', 1)
        s = s.replace('010', '00', 1)
    return s
   
def sc(s):
    return sum(list(map(int, list(s))))

s1 = '0'+'1'*40+'2'*44+'0'
sum1 = sc(s1)
s2= avt(s1)
sum2 = sc(s2)

print(sum1, s1)
print(sum2, s2)

'''
223131313100
313131313100
'''