def avt(x):
	x2 = bin(x)[2:] # получаем двоичную запись числа
	dop = str(x2.count('1') % 2) # вычисляем бит четности
	res = int(x2 + dop, 2) # получаем результат в 10-й СС
	return res

N = 1
while avt(avt(N)) <= 77:
    N += 1
print(N)
