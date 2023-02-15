import turtle as t

t.speed(10)
t.color('green')
t.bgcolor('black')
b = 200

while b > 0:
    t.left(b)
    t.forward(b * 3)
    b = b - 1

t.done()