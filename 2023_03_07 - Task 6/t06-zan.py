'''cnt = 0
for x in range(1, 15):
    for y in range(1, 15):
        if y < -x/3**0.5 + 10 and y > x/3**0.5:
            cnt += 1
print(cnt)
'''
'''
cnt = 0
for x in range(1, 7):
    for y in range(1, 15):
        if y<0.577350269189626*x+4 and \
           y<-0.577350269189626*x+8:
            cnt += 1
print(cnt)
'''
'''
import turtle as t
k = 60
t.left(90)
for i in range(7):
    t.forward(10*k)
    t.right(120)

t.up()
for x in range(0, 12):
    for y in range(0, 12):
        t.goto(x*k, y*k)
        t.dot(4)

t.mainloop()
'''

import turtle as t
k = 30
t.left(90)
for i in range(8):
    t.forward(12*k)
    t.right(90)

t.up()
for x in range(0, 14):
    for y in range(0, 14):
        t.goto(x*k, y*k)
        t.dot(4)

t.mainloop()
