import itertools

def ok(x):
    for i in range(5):
        if x[i]==x[i+1]: # соседние буквы д.б. разными
            return False
    return True

s = 'КАПКАН'
v = list(itertools.permutations(s)) # перестановки букв
v2 = set(v) # убираем дубли из-за одинаковых букв
cnt = 0
for i in v2: # просматриваем все перестановки
    if ok(i): # проверяем что нет АА и КК
        cnt += 1
print(cnt) 
