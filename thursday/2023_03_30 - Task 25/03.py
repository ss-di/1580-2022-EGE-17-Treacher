'''
Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [3532000; 3532160], простые числа. Выведите все найденные простые числа в порядке возрастания, слева от каждого числа выведите его номер по порядку. 
'''

def check(x):
    res = []
    d = 1
    while d*d < x:
        if x % d == 0:
            res += [d, x // d]
        d += 1

    if d*d == x:
        res += [d]

    return res

f = 194455
t = 194500

#f = 1944550
#t = 1945000


for x in range(f, t+1):
    dels = check(x)
    dels.sort()
    if len(dels) == 4:
        print(x, *dels)
