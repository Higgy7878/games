import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    r = 0
    g = 255
    b = randint (0,255)

    w=WIDTH
    h=HEIGHT - 200

    for i in range(20):
        rect= Rect((0,0),(w,h))
        rect.center=150,150
        screen.draw.rect(rect,(r,g,b))

        g=g-10
        r=r+10
        w=w-10
        h=h+10
pgzrun.go()






















































