import itertools

s = 'КАПКАН'
v = list(itertools.permutations(s)) # перестановки букв
v2 = set(v) # убираем дубли из-за одинаковых букв
cnt = 0
for i in v2: # просматриваем все перестановки
    word = ''.join(i)
    # проверяем что нет АА и КК
    if word.count("АА") == word.count("КК") == 0:
        cnt += 1
print(cnt) 
