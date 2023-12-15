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

def delarrows():
    for arrow in arrows:
        arrow.kill()

blocks = sprite.Group()
arrows = sprite.Group()
players = sprite.Group()
window = display.set_mode((1000, 1000))
display.set_caption('BLOCK ATTACK!')
background = transform.scale(image.load('background.png'), (1000, 1000))

#game base
FPS = 60
clock = time.Clock()

player = Player('player0.png', 500, 500, 5, 50, 50)
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
clock = time.Clock()
arrcount = 0

#music
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play(-1)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    keys = key.get_pressed()

    if finish == False:
        if playerhp >= 91 and playerhp<= 100:
            player = Player('player0.png', 500, 500, 5, 50, 50)
        if playerhp >= 81 and playerhp<= 90:
            player = Player('player1.png', 500, 500, 5, 50, 50)
        if playerhp >= 71 and playerhp<= 80:
            player = Player('player2.png', 500, 500, 5, 50, 50)
        if playerhp >= 61 and playerhp<= 70:
            player = Player('player3.png', 500, 500, 5, 50, 50)
        if playerhp >= 51 and playerhp<= 60:
            player = Player('player4.png', 500, 500, 5, 50, 50)
        if playerhp >= 41 and playerhp<= 50:
            player = Player('player5.png', 500, 500, 5, 50, 50)
        if playerhp >= 31 and playerhp<= 40:
            player = Player('player6.png', 500, 500, 5, 50, 50)
        if playerhp >= 21 and playerhp<= 30:
            player = Player('player7.png', 500, 500, 5, 50, 50)
        if playerhp >= 11 and playerhp<= 20:
            player = Player('player8.png', 500, 500, 5, 50, 50)
        players.add(player)
        
        arrcount += 1
        ranarrow = randint(1,62)

        if ranarrow == 1:
            L_arrow = LeftArrow('left_arrow.png', 0, 520, 30, 60, 10)
            arrows.add(L_arrow)

        if ranarrow == 4:
            R_arrow = RightArrow('right_arrow.png', 1000, 520, 30, 60, 10)
            arrows.add(R_arrow)

        if ranarrow == 8:
            U_arrow = UpArrow('down_arrow.png', 520, 0, 30, 10, 60)
            arrows.add(U_arrow)

        if ranarrow == 12:
            D_arrow = DownArrow('up_arrow.png', 520, 1000, 30, 10, 60)
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

        if playerhp <= 0:
            delarrows()
            delblocks()
            mixer.music.pause()
            finish = True
            lose = Player('LOSE.png', 150, 100, 5, 700, 420)
            lose.update()
            restart = Player('restart.png', 250, 590, 5, 500, 100)
            restart.update()


        players.update()
        blocks.update()
        arrows.update()
        blocks.draw(window)
        arrows.draw(window)
        players.draw(window)
        display.update()
        clock.tick(30)
        
    if keys[K_SPACE] and playerhp <= 0:
        finish = False
        playerhp = 100
        mixer.music.unpause()