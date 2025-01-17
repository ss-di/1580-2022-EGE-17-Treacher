'''
Задание 19. 
Найдите значение S, при котором Ваня выигрывает своим первым ходом при любой игре Пети?
Задание 20.
Найдите минимальное и максимальное значение S, при котором у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.
Задание 21
Найдите значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом. 

51 (А. Кабанов) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может убрать из одной из куч один камень или уменьшить количество камней в куче в два раза (если количество камней в куче нечётно, остаётся на 1 камень больше, чем убирается). Например, пусть в одной куче 6, а в другой 9 камней; такую позицию мы будем обозначать (6, 9). За один ход из позиции (6, 9) можно получить любую из четырёх позиций: (5, 9), (3, 9), (6, 8), (6, 5). Игра завершается в тот момент, когда суммарное количество камней в кучах становится не более 32. Победителем считается игрок, сделавший последний ход, то есть первым получивший позицию, в которой в кучах будет 32 или меньше камней. В начальный момент в первой куче было 10 камней, во второй куче – S камней, S > 22.

1 - 45
2 - 46 55
3 - 48
'''

def hod(a, b, mh, h=0):
    if a + b <= 32:
        if h % 2 == 1:
            return 1
        else:
            return 2
    h += 1
    if h > mh:
        return 3
    vars = []
    vars.append(hod(a-1, b, mh, h))
    vars.append(hod(a, b-1, mh, h))
    vars.append(hod((a+1)//2, b, mh, h))
    vars.append(hod(a, (b+1)//2, mh, h))
    if h % 2 == 1:
        if 1 in vars:
            return 1
        elif 3 in vars:
            return 3
        else:
            return 2
    else:
        if 2 in vars:
            return 2
        elif 3 in vars:
            return 3
        else:
            return 1


print("", end = "\t")
for mh in range(1, 5):
    print(mh, end = "\t")
print()

a = 10
for b in range(23, 1000):
    print(b, end="\t")
    for mh in range(1, 5):
        print(hod(a, b, mh), end = "\t")
    print()
