from turtle import *
from math import *
tracer(2)             # speed(0) команды ускорения рисования
hideturtle()          # ht() скрыть изображение черепашки
m = 25                # масштаб
left(90)              # lt(90)
for i in range(7):
  forward(10 * m)     # fd(10*m)
  right(120)          # rt(120)
penup()               # up() поднять перо Черепашки
count = 0             # количество точек, попавших внутрь треугольника
k = tan(pi / 6)       # тангенс угла пи/6 радиан (угла 30 градусов)
for x in range(0, 11):
  for y in range(0, 11):
    goto(x * m, y * m)
    if (y < -k * x + 10  # ниже верхней линии треугольника?
      and y > k * x        # выше нижней линии треугольника?
        and x > 0):   # правее вертикальной линии треугольника?
      dot(5, 'red')   # красная точка (точка попала 
                      # внутрь треугольника)
      count += 1
    else:
      dot(5, 'black') # черная точка (точка не попала 
                      # внутрь треугольника)
  color('red')
  write(count)    # количество красных точек по колонкам
                  # нарастающим итогом
mainloop()            # done()
