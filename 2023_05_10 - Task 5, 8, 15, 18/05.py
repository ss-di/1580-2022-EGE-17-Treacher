# (680y + 256x < A) ∨ (5x + 3y > 11111)


#(5x + 3y > 11111)
x = 0
y = 11111/3 # 3703.666

y = 0
x = 11111/5 # 2222.2

# (680y + 256x < A)
x = 0
y = 3703
A = 680*y + 256*x

y = 0
x = A / 256

print('x = ', x, 'y = ', y)

print(A)