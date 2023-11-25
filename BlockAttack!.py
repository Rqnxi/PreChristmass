from random import randint
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        self.width = width
        self.height = height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class LeftArrow(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.y < 0 or self.rect.y > 1100:
            self.kill

class RightArrow(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill

class UpArrow(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.kill

class DownArrow(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.kill

class Player(GameSprite):
    def update(self):
        GameSprite.reset(self)

def delblocks():        
    for block in blocks:
        block.kill()

window = display.set_mode((1000, 1000))
display.set_caption('BLOCK ATTACK!')
background = transform.scale(image.load('background.png'), (1000, 1000))


#game base
FPS = 60
clock = time.Clock()
blocks = sprite.Group()
arrows = sprite.Group()
player = Player('player.png', 500, 500, 5, 50, 50)
game = True
finish = False


#game cycle
up = False
down = False
left = False
right = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    keys = key.get_pressed()

    if finish == False:
        ranarrow = randint(1,4)
        if ranarrow == 1:
            print('LEFT')
#            L_arrow = LeftArrow('left_arrow.png', 0, 495, 20, 50, 5)
#            arrows.add(L_arrow)
        if ranarrow == 2:
            print('RIGHT')
            R_arrow = RightArrow('right_arrow.png', 1000, 495, 20, 50, 5)
            arrows.add(R_arrow)
        if ranarrow == 3:
            print('UP')
#            U_arrow = LeftArrow('up_arrow.png', 495, 0, 20, 5, 50)
#            arrows.add(U_arrow)
        if ranarrow == 4:
            print('DOWN')
#            D_arrow = LeftArrow('down_arrow.png', 495, 1000, 20, 5, 50)
#            arrows.add(D_arrow)
        if keys[K_LEFT]:
            up = False
            right = False
            left = True
            down = False
        if keys[K_RIGHT]:
            up = False
            right = True
            left = False
            down = False
        if keys[K_UP]:
            up = True
            right = False
            left = False
            down = False
        if keys[K_DOWN]:
            up = False
            right = False
            left = False
            down = True
        if up == True:
            print('up block')
            Ublock = GameSprite('block_up.png', 475, 460, 0, 100, 10)
            delblocks()
            blocks.add(Ublock)

        if down == True:
            print('down block')
            Dblock = GameSprite('block_down.png', 475, 585, 0, 100, 10)
            delblocks()
            blocks.add(Dblock)

        if left == True:
            print('left block')
            Lblock = GameSprite('block_left.png', 450, 470, 0, 10, 100)
            delblocks()
            blocks.add(Lblock)

        if right == True:
            print('right block')
            Rblock = GameSprite('block_right.png', 590, 470, 0, 10, 100)
            delblocks()
            blocks.add(Rblock)

        player.reset()
        player.update()
        blocks.update()
        arrows.update()
        blocks.draw(window)
        arrows.draw(window)
        display.update()