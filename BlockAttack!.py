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
        self.rect.x -= self.speed
        if self.rect.y < 0:
            self.kill

class UpArrow(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill

class DownArrow(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.x < 0:
            self.kill

class Player(GameSprite):
    def update(self):
        GameSprite.reset(self)

def delblocks():        
    for block in blocks:
        block.kill()

blocks = sprite.Group()
arrows = sprite.Group()
players = sprite.Group()
window = display.set_mode((1000, 1000))
display.set_caption('BLOCK ATTACK!')
background = transform.scale(image.load('background.png'), (1000, 1000))

#game base
FPS = 60
clock = time.Clock()

player = Player('player.png', 500, 500, 5, 50, 50)
game = True
finish = False


#game cycle
up = False
down = False
left = False
right = False
BLOCKED = 0
playerhp = 100

#font
font.init()
font = font.SysFont('gamefont.ttf', 70)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    keys = key.get_pressed()

    if finish == False:
        ranarrow = randint(1,62)
        
        player = Player('player.png', 500, 500, 5, 50, 50)
        players.add(player)

        if ranarrow == 1:
            print('LEFT')
            L_arrow = LeftArrow('left_arrow.png', 0, 520, 15, 40, 5)
            arrows.add(L_arrow)
        if ranarrow == 4:
            print('RIGHT')
            R_arrow = RightArrow('right_arrow.png', 1000, 520, 15, 40, 5)
            arrows.add(R_arrow)
        if ranarrow == 8:
            print('UP')
            U_arrow = UpArrow('up_arrow.png', 520, 0, 15, 5, 40)
            arrows.add(U_arrow)
        if ranarrow == 12:
            print('DOWN')
            D_arrow = DownArrow('down_arrow.png', 520, 1000, 15, 5, 40)
            arrows.add(D_arrow)
        
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

            Ublock = GameSprite('block_up.png', 475, 460, 0, 100, 10)
            delblocks()
            blocks.add(Ublock)
        if down == True:

            Dblock = GameSprite('block_down.png', 475, 585, 0, 100, 10)
            delblocks()
            blocks.add(Dblock)
        if left == True:

            Lblock = GameSprite('block_left.png', 450, 470, 0, 10, 100)
            delblocks()
            blocks.add(Lblock)
        if right == True:

            Rblock = GameSprite('block_right.png', 590, 470, 0, 10, 100)
            delblocks()
            blocks.add(Rblock)
        
        collide_list = sprite.groupcollide(arrows, blocks, True, True)
        for i in collide_list:
            BLOCKED += 1
        
        p_collide = sprite.groupcollide(arrows, players, True, True)
        for i in p_collide:
            playerhp -= 1 

        if playerhp <= 100 and playerhp >= 90:
            text_hp = font.render('Health:' + str(playerhp), 1, (255,255,255))
            window.blit(text_hp, (10, 0))
        if playerhp < 90 and playerhp >= 50:
            text_hp = font.render('Health:' + str(playerhp), 1, (255, 165, 0))
            window.blit(text_hp, (10, 0))
        if playerhp < 50:
            text_hp = font.render('Health:' + str(playerhp), 1, (255, 69, 0))
            window.blit(text_hp, (10, 0))
        
        text_count = font.render('BLOCKED:' + str(BLOCKED), 1, (255,255,255))
        window.blit(text_count, (10, 50))

    
        players.update()
        blocks.update()
        arrows.update()
        blocks.draw(window)
        arrows.draw(window)
        players.draw(window)
        display.update()