x = 9**8+3**5-9
x3 = ''
dig = '0123456789ABCDEF'
while x:
    x3 = dig[x%3] + x3
    x //= 3
print( 'Ответ:', x3.count('2') )
