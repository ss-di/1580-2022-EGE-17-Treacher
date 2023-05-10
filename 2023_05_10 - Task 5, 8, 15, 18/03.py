def calc(gl, sg):
    if gl + sg == 18:
        if gl == sg:
            return 1
        else:
            return 0
    return calc(gl+1, sg)*3 + calc(gl, sg+1)*5

sym = 'ЕВЛАМПИЙ'

beg = 'ПИЛАЕВЛА'

print(len(beg))

print(calc(4, 4))