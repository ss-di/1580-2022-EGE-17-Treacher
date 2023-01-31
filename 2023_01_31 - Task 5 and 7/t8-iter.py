import itertools

# строим все размещения с повторениями
p = itertools.product('ШКОЛА', repeat=3)

n = 0
for x in p: # перебираем полученные строки
  if x.count('К') == 1: # проверяем что К встречается 1 раз
    n += 1
print(n)
