from pygame import *

win = display.set_mode((700,500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.png"),(700,500))
sprite1  = transform.scale(image.load("sprite1.png"),(50,50))
sprite2  = transform.scale(image.load("sprite2.png"),(50,50))
x1 = 100
y1 = 350
x2 = 350
y2 = 350
game = True
FPS = 60
clock = time.Clock()

while game:
    win.blit(background,(0,0))
    win.blit(sprite1,(x1,y1))
    win.blit(sprite2,(x2,y2))
    for e  in event.get():
        if e.type==QUIT:
            game = False

    keys_pressed = key.get_pressed()
    
    if keys_pressed[K_UP] and y2>5:
        y2 = y2 - 10
    if keys_pressed[K_DOWN] and y2<395:
        y2+=10
    if keys_pressed[K_LEFT] and x2>5:
        x2-=10
    if keys_pressed[K_RIGHT] and x2<645:
        x2+=10

    if keys_pressed[K_w] and y1>5:
        y1 = y1 - 10
    if keys_pressed[K_s] and y1<395:
        y1+=10
    if keys_pressed[K_a] and x1>5:
        x1-=10
    if keys_pressed[K_d] and x1<645:
        x1+=10

    
    display.update()    
    clock.tick(FPS)