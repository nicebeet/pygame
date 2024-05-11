#створи гру "Лабіринт"!
from pygame import *
win_w = 700
win_h = 500

win = display.set_mode((win_w,win_h))
display.set_caption("Лабіринт")
backround = transform.scale(image.load("background.jpg"),(win_w,win_h))

game = True

mixer.init()
mixer.music.load("jungles.ogg")
mixer_music.play()



class GameSprite(sprite.Sprite):
    def __init__(self,image_name,speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(image_name),(70,70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

player = GameSprite("hero.png",10,10,410,)
cyborg = GameSprite("cyborg.png",10,550,300)
treasure = GameSprite("treasure.png",10,600,410)
while game :
    win.blit(backround,(0,0))
    player.draw()
    cyborg.draw()
    treasure.draw()
    for e in event.get():
        if e.type == QUIT:
            game = False

        
        if event == K_RIGHT:
            move_right = True
        if event == K_LEFT:
            move_left = True
        if event == K_UP:
            move_up = True
        if event == K_DOWN:
            move_down = True


        if event == K_RIGHT:
            move_right = False
        if event == K_LEFT:
            move_left = False
        if event == K_UP:
            move_up = False
        if event == K_DOWN:
            move_down = False
if move_up:
    player.rect.y -= 3
if move_down:
    player.rect.y += 3    
if move_right:
    player.rect.x += 3
if move_left:
    player.rect.x -= 3

    display.update()




