'''
Р-04 (Демо-вариант 2023). Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
– символ «?» означает ровно одну произвольную цифру;
– символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность. Например, маске 123*4?5 соответствуют числа 123405 и 12300405.
Среди натуральных чисел, не превышающих 1010, найдите все числа, соответствующие маске 1?2139*4, делящиеся на 2023 без остатка.
В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 2023.
'''

import fnmatch

f = 2023
t = 10**10

'''
01234567
1?2139*4
'''

cnt = 0
for x in range(f, t+1, 2023):
    s = str(x)
    if fnmatch.fnmatch(s, "1?2139*4"):
        cnt += 1
        print(x)
