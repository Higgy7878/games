import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

s=0
gm=False

bee=Actor("bee")
bee.pos = 100,100

f=Actor("flower")
f.pos = 200,200

def draw():
    screen.blit("background",(0,0))

    f.draw()    
    bee.draw()
    screen.draw.text("Score: "+str(s),color= "black", topleft=(10,10))

    if gm:
        screen.fill("pink")
        screen.draw.text("your final score is "+str(s),midtop=(WIDTH/2,10),fontsize=40,color= "red")

def pf():
    f.x=randint(70,(WIDTH-70))
    f.y=randint(70,(HEIGHT-70))

def tu():
    global gm
    gm=True

def update():
    global s

    if keyboard.left:
        bee.x=bee.x-2
    if keyboard.right:
        bee.x=bee.x+2
    if keyboard.up:
        bee.y=bee.y-2
    if keyboard.down:
        bee.y=bee.y+2

    fc = bee.colliderect(f)
    if fc:
        s=s+1
        pf()

clock.schedule(tu,60.0)

pgzrun.go()





