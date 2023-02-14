for x in range(2, 14):
    z = int('3' + str(x) + '15' + str(x), 15) + \
        1 * int('3' + str(x) + '51') ** 2 + \
        2 * int('3' + str(x) + '51') ** 1 + \
        3 + \
        x ** x + \
        1 * int('1' + str(x) + '3') ** 2 + \
        x * int('1' + str(x) + '3') ** 1 + \
        3 + \
        int('1' + str(x) + '2', x+1)
    if z % 13 == 0:
        z13 = ''
        d = '0123456789ABC'
        while z:
            z13 = d[z % 13] + z13
            z = z // 13
        print(x, z13)