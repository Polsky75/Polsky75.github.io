#shop theme by CleytonKauffman
import pygame
import random
from os import path
from ctypes import *
from math import sqrt

WIDTH = windll.user32.GetSystemMetrics(0)
HEIGHT = windll.user32.GetSystemMetrics(1)
FPS = 100

# Colors RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Creating game and window.
pygame.init()
pygame.mixer.init()  # For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
camera = [0, 0]
button = False
linker = False
button2 = False
linker2 = False
button3 = False
linker3 = False
buttonK = False
linkerK = False
buttonT = False
linkerT = False
buttonRT = False
linkerRT = False
but = False
but2 = False
butt = False
butt2 = False
isBoss = False

def move_camera(x, y):
    camera[0] += x
    camera[1] += y


# Loading assets
img_dir = path.join(path.dirname(__file__), 'img')
rozha_sit = []
for i in range(1, 16):
    filename = 'Rozha_{}.png'.format(i)
    rozha_sit.append(pygame.image.load(path.join(img_dir, filename)).convert())
rozha_run = []
for i in range(1, 38):
    filename = 'RozhaRun_{}.png'.format(i)
    rozha_run.append(pygame.image.load(path.join(img_dir, filename)).convert())
father = []
for i in range(1, 7):
    filename = 'Father_{}.png'.format(i)
    father.append(pygame.image.load(path.join(img_dir, filename)).convert())
rozha_dumb = []
for i in range(1, 22):
    filename = 'RozhaDumb_{}.png'.format(i)
    rozha_dumb.append(pygame.image.load(
        path.join(img_dir, filename)).convert())
mother_dialogue_0 = []
for i in range(1, 2):
    filename = 'q-Moth-0-dialogue-{}.png'.format(i)
    mother_dialogue_0.append(pygame.image.load(path.join(img_dir, filename)).convert())
mother_dialogue_1 = []
for i in range(1, 5):
    filename = 'q-Moth-1-dialogue-{}.png'.format(i)
    mother_dialogue_1.append(pygame.image.load(path.join(img_dir, filename)).convert())
mother_dialogue_2 = []
for i in range(1, 4):
    filename = 'q-Moth-2-dialogue-{}.png'.format(i)
    mother_dialogue_2.append(pygame.image.load(path.join(img_dir, filename)).convert())
mother_dialogue_3 = []
for i in range(1, 4):
    filename = 'q-Moth-3-dialogue-{}.png'.format(i)
    mother_dialogue_3.append(pygame.image.load(path.join(img_dir, filename)).convert())
mother_dialogue_4 = []
for i in range(1, 2):
    filename = 'q-Moth-4-dialogue-{}.png'.format(i)
    mother_dialogue_4.append(pygame.image.load(path.join(img_dir, filename)).convert())
mother_dialogue_5 = []
for i in range(1, 3):
    filename = 'q-Moth-5-dialogue-{}.png'.format(i)
    mother_dialogue_5.append(pygame.image.load(path.join(img_dir, filename)).convert())
father_dialogue_1 = []
for i in range(1, 7):
    filename = 'q-Fath-dialogue-1-{}.png'.format(i)
    father_dialogue_1.append(pygame.image.load(path.join(img_dir, filename)).convert())
filename = 'Cursor.png'
cursor_img = pygame.image.load(path.join(img_dir, filename)).convert()
if isBoss == False:
    field = pygame.image.load(path.join(img_dir, 'Bg.png')).convert()
else:
    field = pygame.image.load(path.join(img_dir, 'Boss_bg.png')).convert()
field_rect = field.get_rect()
screpk = pygame.image.load(path.join(img_dir, 'Skrepk.png')).convert()
screpk_rect = screpk.get_rect()
screpk.set_colorkey(WHITE)
treat_img = pygame.image.load(path.join(img_dir, 'Treat.png')).convert()
treat_rect = treat_img.get_rect()
treat_img.set_colorkey(WHITE)
raretreat_img = pygame.image.load(path.join(img_dir, 'Raretreat.png')).convert()
raretreat_rect = raretreat_img.get_rect()
raretreat_img.set_colorkey(WHITE)
inventory_img = pygame.image.load(
    path.join(img_dir, 'Inventory.png')).convert()
inventory_img.set_colorkey(WHITE)
inventory_rect = inventory_img.get_rect()
inventory_rect.x = WIDTH/2-510
inventory_rect.y = HEIGHT/2-330
start_img = pygame.image.load(
    path.join(img_dir, 'Start.png')).convert()
start_img.set_colorkey(WHITE)
start_rect = start_img.get_rect()
start_rect.x = WIDTH/2-510
start_rect.y = HEIGHT/2-330
lose_img = pygame.image.load(
    path.join(img_dir, 'lose.png')).convert()
lose_img.set_colorkey(WHITE)
lose_rect = lose_img.get_rect()
lose_rect.x = WIDTH/2-510
lose_rect.y = HEIGHT/2-330
saves_img = pygame.image.load(
    path.join(img_dir, 'saves.png')).convert()
saves_img.set_colorkey(WHITE)
saves_rect = start_img.get_rect()
saves_rect.x = WIDTH/2-510
saves_rect.y = HEIGHT/2-330
char_img = pygame.image.load(
    path.join(img_dir, 'char.png')).convert()
char_img.set_colorkey(WHITE)
char_rect = char_img.get_rect()
char_rect.x = WIDTH/2-510
char_rect.y = HEIGHT/2-330

shop_img = pygame.image.load(
    path.join(img_dir, 'shop.png')).convert()
shop_img.set_colorkey(WHITE)
shop_rect = char_img.get_rect()
shop_rect.x = WIDTH/2-510
shop_rect.y = HEIGHT/2-330

kakurzhatka_img = pygame.image.load(
    path.join(img_dir, 'kakurzhatka.png')).convert()
kaPlayer_img = pygame.image.load(
    path.join(img_dir, 'Ka_player.png')).convert()

img20 = pygame.image.load(
    path.join(img_dir, '20%.png')).convert()
img20.set_colorkey(WHITE)
rect20 = img20.get_rect()
img40 = pygame.image.load(
    path.join(img_dir, '40%.png')).convert()
img40.set_colorkey(WHITE)
rect40 = img40.get_rect()
img59 = pygame.image.load(
    path.join(img_dir, '59.5%.png')).convert()
img59.set_colorkey(WHITE)
rect59 = img59.get_rect()
img_ka_badge = pygame.image.load(
    path.join(img_dir, 'Ka_badge.png')).convert()
img_ka_badge.set_colorkey(WHITE)
rect_ka_badge = img_ka_badge.get_rect()
img_treat = pygame.image.load(
    path.join(img_dir, 'Treat_shop.png')).convert()
img_treat.set_colorkey(WHITE)
rect_treat = img_treat.get_rect()
img_raretreat = pygame.image.load(
    path.join(img_dir, 'Raretreat_shop.png')).convert()
img_raretreat.set_colorkey(WHITE)
rect_raretreat = img_raretreat.get_rect()

button_img = pygame.image.load(
    path.join(img_dir, 'Button.png')).convert()
button_img.set_colorkey(WHITE)
button_rect = button_img.get_rect()
button2_img = pygame.image.load(
    path.join(img_dir, 'Button2.png')).convert()
button2_img.set_colorkey(WHITE)
button2_rect = button2_img.get_rect()
button1_img = pygame.image.load(
    path.join(img_dir, 'Button1.png')).convert()
button1_img.set_colorkey(WHITE)
button1_rect = button1_img.get_rect()

bulletCirc1_img = pygame.image.load(
    path.join(img_dir, 'BulletCirc1.png')).convert()
button1_img.set_colorkey(WHITE)
button1_rect = button1_img.get_rect()

bulletCirc2_img = pygame.image.load(
    path.join(img_dir, 'BulletCirc2.png')).convert()
button1_img.set_colorkey(WHITE)
button1_rect = button1_img.get_rect()

boss1_img = pygame.image.load(
    path.join(img_dir, 'Boss1-1.png')).convert()
button1_img.set_colorkey(WHITE)
button1_rect = button1_img.get_rect()
obst = [[0, 0, 30, 310, None], [0, 0, 595, 27, None], [566, 0, 30, 310, None], [
    0, 280, 331, 30, None], [482, 280, 113, 30, None], [278, 45, 262, 113, None], [1200, 496, 136, 63, None], [877,23,864,56,'bridge']]
obst2 = [[420, 186, 10, 10, 'q-Fath'], [1245, 572, 10, 10, 'shop-01'], [86, 165, 10, 10, 'q-Moth1']]
kvartals = [[1747,1000,1425,686]]

# Text
font_name = pygame.font.match_font('Arial')


def draw_text(surf, text, size, x, y,color = BLACK,ori = None):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if ori == None:
        text_rect.x = x
        text_rect.y = y
    else:
        text_rect.x = x - text_rect.width/2
        text_rect.y = y - text_rect.height/2
    surf.blit(text_surface, text_rect)


def show_button(x, y, pos, linker, button, drink, fun = None):
    if fun == None:
        button_rect.x = x
        button_rect.y = y
        screen.blit(button_img, button_rect)
    elif fun == False:
        button1_rect.x = x
        button1_rect.y = y
        screen.blit(button1_img, button1_rect)
    elif fun == True:
        button2_rect.x = x
        button2_rect.y = y        
        screen.blit(button2_img, button2_rect)
    if drink == '20%':
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linker == False:
                if player.inv['20%'][0] > 1:
                    player.inv['20%'][0] -= 1
                    if fun == None:
                        player.liquid += player.effect
                    elif fun == False:
                        player.inv2['20%'] += 1
                else:
                    player.inv['20%'][0] -= 1
                    if fun == None:
                        player.liquid += player.effect
                    elif fun == False:
                        player.inv2['20%'] += 1
                    del(player.inv['20%'])
                    button = False
            elif not pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and not pygame.sprite.collide_rect(Obstacles(rect20.x, rect20.y, rect20.width, rect20.height, None), Obstacles(pos[0], pos[1], 1, 1, None)):
                button = False
            linker = True
        else:
            linker = False
    elif drink == '59%':
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linker == False:
                if player.inv['59%'][0] > 1:
                    player.inv['59%'][0] -= 1
                    if fun == None:
                        player.liquid += 0.25 * player.effect
                        player.isKwave = True
                        player.pyrzhNum += 1
                        if player.maQuests == 5:
                            player.text[5] = "Выпито пыржанки: " + str(player.pyrzhNum) + "/5"
                        player.health += 3
                    elif fun == False:
                        player.inv2['59%'] += 1
                else:
                    player.inv['59%'][0] -= 1
                    if fun == None:
                        player.liquid += 0.25 * player.effect
                        player.isKwave = True
                        player.pyrzhNum += 1
                        if player.maQuests == 5:
                            player.text[5] = "Выпито пыржанки: " + str(player.pyrzhNum) + "/5"
                        player.health += 3
                    elif fun == False:
                        player.inv2['59%'] += 1
                    del(player.inv['59%'])
                    button = False
            elif not pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and not pygame.sprite.collide_rect(Obstacles(rect59.x, rect59.y, rect59.width, rect59.height, None), Obstacles(pos[0], pos[1], 1, 1, None)):
                button = False
            linker = True
        else:
            linker = False
        player.health = min(player.max_health, player.health)
    elif drink == 'ka_badge':
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linker == False:
                if True:
                    player.pyrzha = not player.pyrzha
            elif not pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and not pygame.sprite.collide_rect(Obstacles(rect_ka_badge.x, rect_ka_badge.y, rect_ka_badge.width, rect_ka_badge.height, None), Obstacles(pos[0], pos[1], 1, 1, None)):
                button = False
            linker = True
        else:
            linker = False
    elif drink == 'treat':
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linker == False:
                if player.inv['treat'][0] > 1:
                    player.inv['treat'][0] -= 1
                    if fun == None:
                        player.health += 5
                        if player.maQuests == 4:
                            player.treat_eat += 1
                            player.text[6] = "Употребить 15 печений: " + str(player.treat_eat) + "/15"
                    elif fun == False:
                        player.inv2['treat'] += 1
                else:
                    player.inv['treat'][0] -= 1
                    if fun == None:
                        player.health += 5
                        if player.maQuests == 4:
                            player.treat_eat += 1
                            player.text[6] = "Употребить 15 печений: " + str(player.treat_eat) + "/15"
                    elif fun == False:
                        player.inv2['treat'] += 1
                    del(player.inv['treat'])
                    button = False
            elif not pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and not pygame.sprite.collide_rect(Obstacles(rect_treat.x, rect_treat.y, rect_treat.width, rect_treat.height, None), Obstacles(pos[0], pos[1], 1, 1, None)):
                button = False
            linker = True
        else:
            linker = False
        player.health = min(player.max_health, player.health)
    elif drink == 'raretreat':
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linker == False:
                if player.inv['raretreat'][0] > 1:
                    player.inv['raretreat'][0] -= 1
                    if fun == None:
                        player.health += 30
                        if player.maQuests == 4:
                            player.raretreat_eat += 1
                            player.text[7] = "Продегустировать 3 редких печенья: " + str(player.raretreat_eat) + "/3"
                    elif fun == False:
                        player.inv2['raretreat'] += 1
                else:
                    player.inv['raretreat'][0] -= 1
                    if fun == None:
                        player.health += 30
                        if player.maQuests == 4:
                            player.raretreat_eat += 1
                            player.text[7] = "Продегустировать 3 редких печенья: " + str(player.raretreat_eat) + "/3"
                    elif fun == False:
                        player.inv2['raretreat'] += 1
                    del(player.inv['raretreat'])
                    button = False
            elif not pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and not pygame.sprite.collide_rect(Obstacles(rect_raretreat.x, rect_raretreat.y, rect_raretreat.width, rect_raretreat.height, None), Obstacles(pos[0], pos[1], 1, 1, None)):
                button = False
            linker = True
        else:
            linker = False
        player.health = min(player.max_health, player.health)
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linker == False:
                player.inv['40%'][0] -= 1
                if fun == None:
                    player.liquid += player.effect * 2
                    if random.randrange(1, 4) == 1:
                        player.effect += 500
                    elif random.randrange(1, 3) == 1:
                        player.maximum += 2000
                    else:
                        player.thirst /= 1.25
                    player.health -= random.randrange(1, 21)
                elif fun == False:
                    player.inv2['40%'] += 1
                if player.inv['40%'][0] == 0:
                    button = False
                    del(player.inv['40%'])
            elif not pygame.sprite.collide_rect(Obstacles(x, y, button_rect.width, button_rect.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and not pygame.sprite.collide_rect(Obstacles(rect40.x, rect40.y, rect40.width, rect40.height, None), Obstacles(pos[0], pos[1], 1, 1, None)):
                button = False
            linker = True
        else:
            linker = False
    return [linker, button]

def draw_health_bar(surf, x, y, pct):
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / player.max_health) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, BLACK, outline_rect, 2)

def draw_liquid_bar(surf, x, y, pct):
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / player.maximum) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, BLUE, fill_rect)
    pygame.draw.rect(surf, BLACK, outline_rect, 2)


def draw_tired_bar(surf, x, y, pct):
    BAR_LENGTH = 100
    BAR_HEIGHT = 5
    fill = (pct / 1000) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, (255, 127, 39), fill_rect)
    pygame.draw.rect(surf, BLACK, outline_rect, 2)


# Loading sounds
pygame.mixer.music.load(path.join(path.dirname(__file__), 'Kirlitsa.mid.mp3'))

class Obstacles(pygame.sprite.Sprite):
    def __init__(self, x, y, xx, yy, f):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((xx, yy))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK)
        # self.image.fill(RED)
        self.x = x
        self.y = y
        self.xx = xx
        self.yy = yy
        self.rect.x = x
        self.rect.y = y
        self.f = f
        self.centerx = x + xx/2
        self.centery = y + yy/2

    def update(self):
        self.rect.x = -camera[0] + WIDTH/2 - 200 + self.x
        self.rect.y = -camera[1] + HEIGHT/2 - 200 + self.y


obstacles = pygame.sprite.Group()
for i in obst:
    obstacles.add(Obstacles(i[0], i[1], i[2], i[3], i[4]))
obstacles2 = pygame.sprite.Group()
for i in obst2:
    obstacles2.add(Obstacles(i[0], i[1], i[2], i[3], i[4]))
kvartalses = pygame.sprite.Group()
for i in kvartals:
    kvartalses.add(Obstacles(i[0], i[1], i[2], i[3], None))
obstacles.add(kvartalses)

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cursor_img
        self.image.set_colorkey('WHITE')
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.centerx = x - camera[0]
        self.rect.centery = y - camera[1]
        self.x = x
        self.y = y

class Kakurzhatka(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = kakurzhatka_img
        self.image.set_colorkey('WHITE')
        self.rect = self.image.get_rect()
        self.dirs = [[1,0,180],[0.75,0.25,202.5],[0.5,0.5,225],[0.25,0.75,247.5],[0,1,270],[-0.25,0.75,292.5],[-0.5,0.5,315],[-0.75,0.25,337.5],[-1,0,0],[-0.75,-0.25,22.5],[-0.5,-0.5,45],[-0.25,-0.75,67.5],[0,-1,90],[0.25,-0.75,112.5],[0.5,-0.5,135],[0.75,-0.25,157.5]]
        self.dir = self.dirs[random.randrange(0,16)]
        self.is_stay = True 
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def update(self,x,y):
        self.image = kakurzhatka_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, -self.dir[2] - 90)
        self.x += self.dir[0]
        self.y += self.dir[1] 
        self.rect.x = -camera[0] + WIDTH/2 - 200 + self.x
        self.rect.y = -camera[1] + HEIGHT/2 - 200 + self.y


# Creating player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.firzt_quest_pyrzha = False
        self.pyrzha = False
        self.effect = 6000
        self.maximum = 10000
        self.thirst = 1
        self.liquid = 10000
        self.tired = 1000
        self.dolb = 0
        self.inv = {'20%': [0, 0, 0], '40%': [0, 0, 0], '59%': [0, 0, 0], 'treat': [0, 0, 0], 'raretreat': [0, 0, 0], 'ka_badge': [0, 0, 0]}
        self.quest = {}
        self.beats = 0
        self.skrepks = 0
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.runx = 0
        self.runy = 0
        self.img = 1
        self.img2 = 0
        self.col_img = True
        self.activity = 'run'
        self.is_stay = True
        self.dumb = False
        pygame.sprite.Sprite.__init__(self)
        self.image = rozha_run[0]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rot = 0
        self.new_rot = 0
        self.rotate = 0
        self.isKwave = False
        self.text = ["","","","","","","",""]
        self.pyrzhNum = 0
        self.kaNum = 0
        self.faQuests = 0
        self.health = 100
        self.max_health = 100
        self.maQuests = 0
        self.kyrp_num = 0
        self.sink_num = 0
        self.kveat_num = 0
        self.wage_num = 0
        self.treat_num = 0
        self.treat_eat = 0
        self.raretreat_eat = 0
    def update(self, x, y):
        if self.pyrzha == True and keystate[pygame.K_w]:
            self.image = kaPlayer_img
            self.tired += 1
        elif self.is_stay == True:
            self.image = rozha_run[max(0, min(int(self.img-1), 36))]
        elif self.dumb == True:
            self.image = rozha_dumb[int(self.img-1)]
        else:
            self.image = rozha_sit[int(self.img2/2)]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x - camera[0]
        self.rect.centery = self.y - camera[1]
        if self.activity == 'run' or (self.pyrzha == True and keystate[pygame.K_w]):
            self.run(x, y)
        elif self.activity == 'dumb':
            self.to_dumb()
        elif self.activity == 'undumb':
            self.to_dumb(False)
        else:
            self.sit()
        if sqrt((x-self.rect.centerx)**2+(y-self.rect.centery)**2) <= 1:
            self.activity = 'sit'
        try:
            if self.activity == 'run':
                move_camera((x-self.rect.centerx)/sqrt((x-self.rect.centerx)**2+(y-self.rect.centery)**2)/2,
                            (y-self.rect.centery)/sqrt((x-self.rect.centerx)**2+(y-self.rect.centery)**2)/2)
            else:
                move_camera((self.rect.centerx-WIDTH/2)/sqrt((self.rect.centerx-WIDTH/2)**2+(self.rect.centery-HEIGHT/2)**2)/2,
                            (self.rect.centery-HEIGHT/2)/sqrt((self.rect.centerx-WIDTH/2)**2+(self.rect.centery-HEIGHT/2)**2)/2)
        except:
            pass
        old_center = self.rect.center
        try:
            if self.is_stay == True:
                if (y-self.rect.centery)/sqrt((x-self.rect.centerx)**2+(y-self.rect.centery)**2) < 0:
                    self.new_rot = 180 - \
                        ((x-self.rect.centerx)/sqrt(abs((x-self.rect.centerx)
                                                        ** 2+(y-self.rect.centery)**2))*90)
                else:
                    self.new_rot = (
                        x-self.rect.centerx)/sqrt(abs((x-self.rect.centerx)**2+(y-self.rect.centery)**2))*90
                self.rotate = self.new_rot - self.rot
                if self.rotate > 180:
                    self.rotate -= 360
                elif self.rotate < -180:
                    self.rotate += 360
                if self.rot > 360:
                    self.rot -= 360
                elif self.rot < 0:
                    self.rot += 360
                if self.rotate > 5:
                    self.rotate = 5
                elif self.rotate < -5:
                    self.rotate = -5
                self.rot += self.rotate
            self.image = pygame.transform.rotate(self.image, self.rot)
        except:
            self.image = pygame.transform.rotate(self.image, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        try:
            cursor.move((x-self.rect.centerx)/sqrt((x-self.rect.centerx)**2+(y-self.rect.centery)**2)*40 +
                        self.x, (y-self.rect.centery)/sqrt((x-self.rect.centerx)**2+(y-self.rect.centery)**2)*40+self.y)
        except:
            pass

    def run(self, x, y):
        self.tired -= 1
        if self.is_stay == False:
            if(self.img2 > 1):
                self.img2 -= 1
            else:
                self.is_stay = True
        else:
            if keystate[pygame.K_SPACE]:
                self.activity = 'sit'
            try:
                if sqrt((x-self.x)**2+(y-self.y)**2) >= 1 and player.tired > 0:
                    self.runx = (x-self.rect.centerx)/sqrt((x -
                                                            self.rect.centerx)**2+(y-self.rect.centery)**2)
                    if self.pyrzha == True and keystate[pygame.K_w]:
                        self.x += self.runx * 1.5
                    else:
                        self.x += self.runx
                    self.runy = (y-self.rect.centery)/sqrt((x -
                                                            self.rect.centerx)**2+(y-self.rect.centery)**2)
                    if self.pyrzha == True and keystate[pygame.K_w]:
                        self.y += self.runy
                    else:
                        self.y += self.runy 
                else:
                    self.activity = 'sit'
            except:
                pass
        if self.col_img:
            self.img += 1
        else:
            self.img -= 1
        if self.img == 37 or self.img == 1:
            self.col_img = not self.col_img
        else:
            pass

    def sit(self):
        self.tired += 2
        if self.img > 19:
            self.img -= 1
        elif self.img < 19:
            self.img += 1
        else:
            self.is_stay = False
            if(self.img2 < 29):
                self.img2 += 1
            else:
                if keystate[pygame.K_SPACE] and not pygame.sprite.spritecollide(cursor, obstacles, False):
                    self.activity = 'run'

    def to_dumb(self, isr=True):
        self.tired -= 1
        if isr:
            if self.img > 19 and not self.dumb:
                self.img -= 1
            elif self.img < 19 and not self.dumb:
                self.img += 1
            elif self.img == 19 and not self.dumb:
                self.img == 11
                self.is_stay = False
                self.dumb = True
                self.help_var = True
                self.beats += 1
                try:
                    player.text[0] = "Отцовский квест:" 
                    player.text[1] = "Побиться головой об стенку: " + str(player.beats) + "/" + str(player.quest['dumb'])
                except:
                    pass
                self.dolb += 0.01
            else:
                if self.img > 1 and self.help_var and not pygame.sprite.spritecollide(player, obstacles, False):
                    self.img -= 0.5
                    self.x += self.runx
                    self.y += self.runy
                else:
                    self.help_var = False
                    if self.img <= 19.5:
                        self.img += 0.5
                        self.x -= self.runx
                        self.y -= self.runy
                    else:
                        self.dumb = False
                        self.activity = 'sit'
                        self.img = 19
                        self.sit()
        else:
            if self.img > 19 and not self.dumb:
                self.img -= 1
            elif self.img < 19 and not self.dumb:
                self.img += 1
            elif self.img == 19 and not self.dumb:
                self.img = 11
                self.is_stay = False
                self.dumb = True
                self.help_var = True
                self.beats += 1
                try:
                    player.text[0] = "Дедовский квест:" 
                    player.text[1] = "Побиться головой об стенку: " + str(player.beats) + "/" + str(player.quest['dumb'])
                except:
                    pass
                self.dolb += 0.01
            else:
                if self.img <= 19.5:
                    self.img += 0.5
                    self.x -= self.runx
                    self.y -= self.runy
                else:
                    self.dumb = False
                    self.activity = 'sit'
                    self.img = 19
                    self.sit()

class Father(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = father[0]
        self.img = 0
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        # self.image.fill(RED)
        self.rect.x = 372
        self.rect.y = 56
        self.x = 372
        self.y = 56
        self.cadr = 0

    def update(self, x, y):
        self.cadr = min(600, max(0, self.cadr))
        if self.cadr >= 500:
            self.img = 5
        elif self.cadr >= 400:
            self.img = 4
        elif self.cadr >= 300:
            self.img = 3
        elif self.cadr >= 200:
            self.img = 2
        elif self.cadr >= 100:
            self.img = 1
        else:
            self.img = 0
        self.image = father[self.img]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = -camera[0] + WIDTH/2 - 200 + self.x
        self.rect.y = -camera[1] + HEIGHT/2 - 200 + self.y

class Questses(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cadr_q_moth_0 = 0
        self.q_moth_0 = False
        self.cadr_q_moth_1 = 0
        self.q_moth_1 = False
        self.cadr_q_moth_2 = 0
        self.q_moth_2 = False
        self.cadr_q_moth_3 = 0
        self.q_moth_3 = False
        self.cadr_q_moth_4 = 0
        self.q_moth_4 = False
        self.cadr_q_moth_5 = 0
        self.q_moth_5 = False
        self.cadr_q_fath_1 = 0
        self.q_fath_1 = False
        self.image = mother_dialogue_1[self.cadr_q_moth_1]
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect() 
        self.rect.x = 30
        self.rect.y = 30

    def update(self):
        if self.q_moth_0:
            if self.cadr_q_moth_0 > 0:
                self.cadr_q_moth_0 = 0
                self.q_moth_0 = False
            self.image = mother_dialogue_0[self.cadr_q_moth_0]
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect() 
            self.rect.x = 30
            self.rect.y = 30
        elif self.q_moth_1:
            if self.cadr_q_moth_1 > 3:
                self.cadr_q_moth_1 = 0
                self.q_moth_1 = False
            self.image = mother_dialogue_1[self.cadr_q_moth_1]
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect() 
            self.rect.x = 30
            self.rect.y = 30
        elif self.q_moth_2:
            if self.cadr_q_moth_2 > 2:
                self.cadr_q_moth_2 = 0
                self.q_moth_2 = False
            self.image = mother_dialogue_2[self.cadr_q_moth_2]
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect() 
            self.rect.x = 30
            self.rect.y = 30
        elif self.q_moth_3:
            if self.cadr_q_moth_3 > 2:
                self.cadr_q_moth_3 = 0
                self.q_moth_3 = False
            self.image = mother_dialogue_3[self.cadr_q_moth_3]
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect() 
            self.rect.x = 30
            self.rect.y = 30
        if self.q_moth_4:
            if self.cadr_q_moth_4 > 0:
                self.cadr_q_moth_4 = 0
                self.q_moth_4 = False
            self.image = mother_dialogue_4[self.cadr_q_moth_4]
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect() 
            self.rect.x = 30
            self.rect.y = 30
        if self.q_moth_5:
            if self.cadr_q_moth_5 > 1:
                self.cadr_q_moth_5 = 0
                self.q_moth_5 = False
            self.image = mother_dialogue_5[self.cadr_q_moth_5]
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect() 
            self.rect.x = 30
            self.rect.y = 30
        elif self.q_fath_1:
            if self.cadr_q_fath_1 > 5:
                self.cadr_q_fath_1 = 0
                self.q_fath_1 = False
            self.image = father_dialogue_1[self.cadr_q_fath_1]
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect() 
            self.rect.x = 30
            self.rect.y = 30

class Screpki(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = screpk
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.dirs = [[1,0,180],[0.75,0.25,202.5],[0.5,0.5,225],[0.25,0.75,247.5],[0,1,270],[-0.25,0.75,292.5],[-0.5,0.5,315],[-0.75,0.25,337.5],[-1,0,0],[-0.75,-0.25,22.5],[-0.5,-0.5,45],[-0.25,-0.75,67.5],[0,-1,90],[0.25,-0.75,112.5],[0.5,-0.5,135],[0.75,-0.25,157.5]]
        self.dir = self.dirs[random.randrange(0,16)]
        self.is_stay = True 
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.stop = False
        self.timer = 100

    def update(self, x, y):
        self.image = screpk
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, -self.dir[2] - 90)
        if not self.stop:
            self.x += self.dir[0]
            self.y += self.dir[1]
        self.rect.x = -camera[0] + WIDTH/2 - 200 + self.x
        self.rect.y = -camera[1] + HEIGHT/2 - 200 + self.y
        if pygame.sprite.spritecollide(self, obstacles, False) == []:
            self.timer -= 1
        if self.timer <= 0:
            self.stop = True
            self.timer = 100

class Treats(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = treat_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.dirs = [[1,0,180],[0.75,0.25,202.5],[0.5,0.5,225],[0.25,0.75,247.5],[0,1,270],[-0.25,0.75,292.5],[-0.5,0.5,315],[-0.75,0.25,337.5],[-1,0,0],[-0.75,-0.25,22.5],[-0.5,-0.5,45],[-0.25,-0.75,67.5],[0,-1,90],[0.25,-0.75,112.5],[0.5,-0.5,135],[0.75,-0.25,157.5]]
        self.dir = self.dirs[random.randrange(0,16)]
        self.is_stay = True 
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.stop = False
        self.timer = 100

    def update(self, x, y):
        self.image = treat_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, -self.dir[2] - 90)
        if not self.stop:
            self.x += self.dir[0]
            self.y += self.dir[1]
        self.rect.x = -camera[0] + WIDTH/2 - 200 + self.x
        self.rect.y = -camera[1] + HEIGHT/2 - 200 + self.y
        if pygame.sprite.spritecollide(self, obstacles, False) == []:
            self.timer -= 1
        if self.timer <= 0:
            self.stop = True
            self.timer = 100

class Raretreats(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = raretreat_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.dirs = [[1,0,180],[0.75,0.25,202.5],[0.5,0.5,225],[0.25,0.75,247.5],[0,1,270],[-0.25,0.75,292.5],[-0.5,0.5,315],[-0.75,0.25,337.5],[-1,0,0],[-0.75,-0.25,22.5],[-0.5,-0.5,45],[-0.25,-0.75,67.5],[0,-1,90],[0.25,-0.75,112.5],[0.5,-0.5,135],[0.75,-0.25,157.5]]
        self.dir = self.dirs[random.randrange(0,16)]
        self.is_stay = True 
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.stop = False
        self.timer = 100

    def update(self, x, y):
        self.image = raretreat_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, -self.dir[2] - 90)
        if not self.stop:
            self.x += self.dir[0]
            self.y += self.dir[1]
        self.rect.x = -camera[0] + WIDTH/2 - 200 + self.x
        self.rect.y = -camera[1] + HEIGHT/2 - 200 + self.y
        if pygame.sprite.spritecollide(self, obstacles, False) == []:
            self.timer -= 1
        if self.timer <= 0:
            self.stop = True
            self.timer = 100
all_sprites = pygame.sprite.Group()
questseses = pygame.sprite.Group()
kakurzhatkas = pygame.sprite.Group()
screpkas = pygame.sprite.Group()
treats_group = pygame.sprite.Group()
raretreats_group = pygame.sprite.Group()
player = Player()
fath = Father()
cursor = Cursor()
questses = Questses()
all_sprites.add(fath, player, cursor)
questseses.add(questses)
pygame.mixer.music.play(loops=-1)
ticks = pygame.time.get_ticks()
# Game cycle
running = True
slide = 'start'
while running:
    if slide == 'lose':
        screen.fill(RED)
        screen.blit(lose_img, lose_rect)
        for event in pygame.event.get():
            # Check window's closing
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                running = False
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_rect(Obstacles(pos[0], pos[1], 1, 1, None), Obstacles(292+start_rect.x, 409+start_rect.y, 653, 109, None)):
            player.inv = {} 
            player.quest = {}
            player.x = WIDTH/2
            player.y = HEIGHT/2
            player.beats = 0
            player.skrepks = 0
            camera = [0,0]
            player.maximum = 10000
            player.effectivity = 6000
            player.thirst = 1
            player.liquid = 10000
            player.dolb = 0
            player.activity = 'sit'
            player.firzt_quest_pyrzha = False
            player.kaNum = 0
            player.pyrzhNum = 0
            player.faQuests = 0
            player.isKwave = False
            player.pyrzha = False
            player.firzt_quest_pyrzha = False
            player.health, player.max_health = 100, 100 
            slide = 'game'
        # After all, turn the screen
        pygame.display.flip()
    elif slide == 'start':
        screen.fill(GREEN)
        screen.blit(start_img, start_rect)
        for event in pygame.event.get():
            # Check window's closing
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                running = False
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_rect(Obstacles(pos[0], pos[1], 1, 1, None), Obstacles(292+start_rect.x, 409+start_rect.y, 653, 109, None)):
            slide = 'saves'
            linker = False
        # After all, turn the screen
        pygame.display.flip()
    elif slide == 'saves':
        screen.fill(GREEN)
        screen.blit(saves_img, saves_rect)
        for event in pygame.event.get():
            # Check window's closing
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                running = False
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.sprite.collide_rect(Obstacles(pos[0], pos[1], 1, 1, None), Obstacles(291+start_rect.x, 108+start_rect.y, 653, 109, None)) and linker == True:
                slide = 'game'
                save = 'file.txt'
                try:
                    with open(save, 'r') as file:
                        camera = [float(i) for i in list(file)[5].split(' ')]
                    with open(save, 'r') as file:
                        player.skrepks = int(list(file)[0])
                    with open(save, 'r') as file:
                        player.x = float(list(file)[1])
                    with open(save, 'r') as file:
                        player.y = float(list(file)[2])
                    with open(save, 'r') as file:
                        player.liquid = float(list(file)[3])
                    with open(save, 'r') as file:
                        player.tired = float(list(file)[4])
                    with open(save, 'r') as file:
                        player.inv['20%'][0], player.inv['40%'][0], player.inv['59%'][0], player.inv['20%'][1], player.inv['40%'][1], player.inv['59%'][1], player.inv['20%'][2], player.inv['40%'][2], player.inv['59%'][2]= [
                            int(i) for i in list(file)[6].split(' ')]
                    with open(save, 'r') as file:
                        player.maximum = float(list(file)[7])
                    with open(save, 'r') as file:
                        player.effect = float(list(file)[8])
                    with open(save, 'r') as file:
                        player.thirst = float(list(file)[9])
                    with open(save, 'r') as file:
                        player.beats, player.quest['dumb'] = [
                            int(i) for i in list(file)[10].split(' ')]
                    with open(save, 'r') as file:
                        player.dolb = float(list(file)[11])
                    with open(save, 'r') as file:    
                        player.kaNum, player.pyrzhNum, player.faQuests = [int(i) for i in list(file)[12].split(' ')]
                    with open(save, 'r') as file:
                        player.firzt_quest_pyrzha = int(list(file)[13])
                    with open(save, 'r') as file:
                        player.inv['treat'][0], player.inv['treat'][1], player.inv['treat'][2]  = [int(i) for i in list(file)[14].split(' ')]  
                    with open(save, 'r') as file:
                        player.inv['raretreat'][0], player.inv['raretreat'][1], player.inv['raretreat'][2]  = [int(i) for i in list(file)[15].split(' ')]  
                    with open(save, 'r') as file:
                        player.health = int(list(file)[16])
                    with open(save, 'r') as file:
                        player.maQuests = int(list(file)[17])
                        if player.maQuests == 1:
                            with open(save, 'r') as file:
                                player.kyrp_num, player.sink_num = [int(i) for i in list(file)[18].split(' ')]
                        elif player.maQuests == 2:
                            with open(save, 'r') as file:
                                player.kyrp_num = int(list(file)[18])
                        elif player.maQuests == 3:
                            with open(save, 'r') as file:
                                player.kveat_num, player.wage_num, player.treat_num = [int(i) for i in list(file)[18].split(' ')]
                        elif player.maQuests == 4:
                            with open(save, 'r') as file:
                                player.kveat_num, player.wage_num, player.treat_eat, player.raretreat_eat = [int(i) for i in list(file)[18].split(' ')]
                    if player.inv['20%'][0] <= 0:
                        del(player.inv['20%'])
                    if player.inv['40%'][0] <= 0:
                        del(player.inv['40%'])
                    if player.inv['59%'][0] <= 0:
                        del(player.inv['59%'])
                    if player.inv['treat'][0] <= 0:
                        del(player.inv['treat'])
                    if player.inv['raretreat'][0] <= 0:
                        del(player.inv['raretreat'])
                except:
                    pass
            elif pygame.sprite.collide_rect(Obstacles(pos[0], pos[1], 1, 1, None), Obstacles(291+start_rect.x, 258+start_rect.y, 653, 109, None)) and linker == True:
                slide = 'game'
                save = 'filf.txt'
                try:
                    with open(save, 'r') as file:
                        camera = [float(i) for i in list(file)[5].split(' ')]
                    with open(save, 'r') as file:
                        player.skrepks = int(list(file)[0])
                    with open(save, 'r') as file:
                        player.x = float(list(file)[1])
                    with open(save, 'r') as file:
                        player.y = float(list(file)[2])
                    with open(save, 'r') as file:
                        player.liquid = float(list(file)[3])
                    with open(save, 'r') as file:
                        player.tired = float(list(file)[4])
                    with open(save, 'r') as file:
                        player.inv['20%'][0], player.inv['40%'][0], player.inv['59%'][0], player.inv['20%'][1], player.inv['40%'][1], player.inv['59%'][1], player.inv['20%'][2], player.inv['40%'][2], player.inv['59%'][2] = [
                            int(i) for i in list(file)[6].split(' ')]
                    with open(save, 'r') as file:
                        player.maximum = float(list(file)[7])
                    with open(save, 'r') as file:
                        player.effect = float(list(file)[8])
                    with open(save, 'r') as file:
                        player.thirst = float(list(file)[9])
                    with open(save, 'r') as file:
                        player.beats, player.quest['dumb'] = [int(i) for i in list(file)[10].split(' ')]
                    with open(save, 'r') as file:
                        player.dolb = float(list(file)[11])
                    with open(save, 'r') as file:    
                        player.kaNum, player.pyrzhNum, player.faQuests = [int(i) for i in list(file)[12].split(' ')]   
                    with open(save, 'r') as file:
                        player.firzt_quest_pyrzha = int(list(file)[13])  
                    with open(save, 'r') as file:
                        player.inv['treat'][0], player.inv['treat'][1], player.inv['treat'][2]  = [int(i) for i in list(file)[14].split(' ')]           
                    with open(save, 'r') as file:
                        player.inv['raretreat'][0], player.inv['raretreat'][1], player.inv['raretreat'][2]  = [int(i) for i in list(file)[15].split(' ')] 
                    with open(save, 'r') as file:
                        player.health = int(list(file)[16]) 
                    with open(save, 'r') as file:
                        player.maQuests = int(list(file)[17])
                        if player.maQuests == 1:
                            with open(save, 'r') as file:
                                player.kyrp_num, player.sink_num = [int(i) for i in list(file)[18].split(' ')]
                        elif player.maQuests == 2:
                            with open(save, 'r') as file:
                                player.kyrp_num = int(list(file)[18])
                        elif player.maQuests == 3:
                            with open(save, 'r') as file:
                                player.kveat_num, player.wage_num, player.treat_num = [int(i) for i in list(file)[18].split(' ')]
                        elif player.maQuests == 4:
                            with open(save, 'r') as file:
                                player.kveat_num, player.wage_num, player.treat_eat, player.raretreat_eat = [int(i) for i in list(file)[18].split(' ')]
                    if player.inv['20%'][0] <= 0:
                        del(player.inv['20%'])
                    if player.inv['40%'][0] <= 0:
                        del(player.inv['40%'])
                    if player.inv['59%'][0] <= 0:
                        del(player.inv['59%'])
                    if player.inv['treat'][0] <= 0:
                        del(player.inv['treat'])
                    if player.inv['raretreat'][0] <= 0:
                        del(player.inv['raretreat'])
                except:
                    pass
            elif pygame.sprite.collide_rect(Obstacles(pos[0], pos[1], 1, 1, None), Obstacles(291+start_rect.x, 409+start_rect.y, 653, 109, None)) and linker == True:
                save = 'filg.txt'
                try:
                    with open(save, 'r') as file:
                        camera = [float(i) for i in list(file)[5].split(' ')]
                    with open(save, 'r') as file:
                        player.skrepks = int(list(file)[0])
                    with open(save, 'r') as file:
                        player.x = float(list(file)[1])
                    with open(save, 'r') as file:
                        player.y = float(list(file)[2])
                    with open(save, 'r') as file:
                        player.liquid = float(list(file)[3])
                    with open(save, 'r') as file:
                        player.tired = float(list(file)[4])
                    with open(save, 'r') as file:
                        player.inv['20%'][0], player.inv['40%'][0], player.inv['59%'][0], player.inv['20%'][1], player.inv['40%'][1], player.inv['59%'][1], player.inv['20%'][2], player.inv['40%'][2], player.inv['59%'][2]= [
                            int(i) for i in list(file)[6].split(' ')]
                    with open(save, 'r') as file:
                        player.maximum = float(list(file)[7])
                    with open(save, 'r') as file:
                        player.effect = float(list(file)[8])
                    with open(save, 'r') as file:
                        player.thirst = float(list(file)[9]) 
                    with open(save, 'r') as file:
                        player.beats, player.quest['dumb'] = [int(i) for i in list(file)[10].split(' ')]
                    with open(save, 'r') as file:
                        player.dolb = float(list(file)[11])
                    with open(save, 'r') as file:    
                        player.kaNum, player.pyrzhNum, player.faQuests = [int(i) for i in list(file)[12].split(' ')]   
                    with open(save, 'r') as file:
                        player.firzt_quest_pyrzha = int(list(file)[13])   
                    with open(save, 'r') as file:
                        player.inv['raretreat'][0], player.inv['raretreat'][1], player.inv['raretreat'][2]  = [int(i) for i in list(file)[15].split(' ')]  
                    with open(save, 'r') as file:
                        player.health = int(list(file)[16])
                    with open(save, 'r') as file:
                        player.maQuests = int(list(file)[17])
                        if player.maQuests == 1:
                            with open(save, 'r') as file:
                                player.kyrp_num, player.sink_num = [int(i) for i in list(file)[18].split(' ')]
                        elif player.maQuests == 2:
                            with open(save, 'r') as file:
                                player.kyrp_num = int(list(file)[18])
                        elif player.maQuests == 3:
                            with open(save, 'r') as file:
                                player.kveat_num, player.wage_num, player.treat_num = [int(i) for i in list(file)[18].split(' ')]
                        elif player.maQuests == 4:
                            with open(save, 'r') as file:
                                player.kveat_num, player.wage_num, player.treat_eat, player.raretreat_eat = [int(i) for i in list(file)[18].split(' ')]
                    if player.inv['20%'][0] <= 0:
                        del(player.inv['20%'])
                    if player.inv['40%'][0] <= 0:
                        del(player.inv['40%'])
                    if player.inv['59%'][0] <= 0:
                        del(player.inv['59%'])
                    if player.inv['treat'][0] <= 0:
                        del(player.inv['treat'])  
                    if player.inv['20%'][0] <= 0:
                        del(player.inv['20%'])
                    if player.inv['40%'][0] <= 0:
                        del(player.inv['40%'])
                    if player.inv['59%'][0] <= 0:
                        del(player.inv['59%'])
                    if player.inv['treat'][0] <= 0:
                        del(player.inv['treat'])  
                    if player.inv['raretreat'][0] <= 0:
                        del(player.inv['raretreat'])                     
                except:
                    pass     
                slide = 'game'
        else:
            linker = True
        # After all, turn the screen
        pygame.display.flip()
        if player.firzt_quest_pyrzha:
            player.inv['ka_badge'] = [1,43,263]
        if player.maQuests == 1:
            player.text[3] = "Синяя Стенка (от Ржалии): " 
            player.text[4] = "Побиться головой об кирпичную стенку 75 раз: " + str(player.kyrp_num) + "/75"
            player.text[5] = "Купить синьку 3 раза: " + str(player.sink_num) + "/3"
            player.text[6] = '' 
            player.text[7] = '' 
        elif player.maQuests == 2:
            player.text[3] = "Экономия И Экономика (от Ржалии): " 
            player.text[4] = "Побиться головой об кирпичную стенку 150 раз: " + str(player.kyrp_num) + "/150"
            player.text[5] = "Накопить 50 скрепок к моменту завершения квеста: " + str(player.skrepks) + "/50"
            player.text[6] = ""
            player.text[7] = ""
        elif player.maQuests == 3:
            player.text[3] = "Общественное Место (от Ржалии): " 
            player.text[4] = "Побиться головой о кирпичное здание с красной крышей 40 раз: " + str(player.kveat_num) + "/40"
            player.text[5] = "Получить 10 скрепок от довольных жителей: " + str(player.wage_num) + "/10"
            player.text[6] = "Подобрать 1 печенье: " + str(player.treat_num) + "/1"
            player.text[7] = ""
        elif player.maQuests == 4:
            player.text[3] = "Общественное Место 2 (от Ржалии): " 
            player.text[4] = "Побиться головой о кирпичное здание с красной крышей 175 раз: " + str(player.kveat_num) + "/175"
            player.text[5] = "Получить 35 скрепок от довольных жителей: " + str(player.wage_num) + "/35"
            player.text[6] = "Употребить 15 печений: " + str(player.treat_eat) + "/15"
        if player.maQuests == 4:
            player.text[7] = "Продегустировать 3 редких печенья: " + str(player.raretreat_eat) + "/3"
        elif player.maQuests == 5:
            player.text[3] = "В погоне за пыржей (от Ржалии): " 
            player.text[4] = "Обкукуцано какуржаток: " + str(player.kaNum) + "/15"
            player.text[5] = "Выпито пыржанки: " + str(player.pyrzhNum) + "/5"
            player.text[6] = "Выполнено отцовских квестов: " + str(player.faQuests) + "/10"
    elif slide == 'game':
        try:
            if player.inv['20%'][0] <= 0:
                del(player.inv['20%'])
            if player.inv['40%'][0] <= 0:
                del(player.inv['40%'])
            if player.inv['59%'][0] <= 0:
                del(player.inv['59%']) 
            if player.inv['treat'][0] <= 0:
                del(player.inv['treat'])
            if player.inv['raretreat'][0] <= 0:
                del(player.inv['raretreat'])     
        except:
            pass
        player.liquid -= player.thirst
        if player.liquid > player.maximum:
            player.liquid = player.maximum
        elif player.liquid < 0:
            slide = 'lose'
        if player.health <= 0:
            slide = 'lose'
        if player.tired > 1000:
            player.tired = 1000
        field_rect.x = -camera[0]+WIDTH/2-200
        field_rect.y = -camera[1]+HEIGHT/2-200
        screen.fill(GREEN)
        screen.blit(field, field_rect)
        draw_health_bar(screen, 175, 25, player.health)
        draw_liquid_bar(screen, 175, 45, player.liquid)
        draw_tired_bar(screen, 175, 60, player.tired)
        pos = pygame.mouse.get_pos()
        # Checking FPS
        clock.tick(FPS)
        # Event
        for event in pygame.event.get():
            # Check window's closing
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                running = False
            if keystate[pygame.K_e] and pygame.time.get_ticks()-ticks > 500:
                slide = 'inv'
                ticks = pygame.time.get_ticks()
            if keystate[pygame.K_q] and pygame.time.get_ticks()-ticks > 500:
                slide = 'char'
                ticks = pygame.time.get_ticks()
            if keystate[pygame.K_RIGHT]:
                if questses.q_moth_0:
                    questses.cadr_q_moth_0 += 1
                elif questses.q_moth_1:
                    questses.cadr_q_moth_1 += 1
                elif questses.q_moth_2:
                    questses.cadr_q_moth_2 += 1
                elif questses.q_moth_3:
                    questses.cadr_q_moth_3 += 1
                elif questses.q_moth_4:
                    questses.cadr_q_moth_4 += 1
                elif questses.q_moth_5:
                    questses.cadr_q_moth_5 += 1
                elif questses.q_fath_1:
                    questses.cadr_q_fath_1 += 1
        # Update
        all_sprites.update(pos[0], pos[1])
        obstacles.update()
        obstacles2.update()
        questseses.update()
        # Dumb
        if pygame.sprite.spritecollide(cursor, obstacles, False) and player.is_stay and player.activity == 'run':
            player.activity = 'dumb'
            hits = pygame.sprite.spritecollide(cursor, obstacles, False) 
            if player.maQuests == 1:   
                for hit in hits:
                    if hit.f == 'bridge':
                        print("ABOBA")
                        player.kyrp_num += 1
                        player.text[4] = player.text[4] = "Побиться головой об кирпичную стенку 75 раз: " + str(player.kyrp_num) + "/75"
            if pygame.sprite.spritecollide(cursor, kvartalses, False) or pygame.sprite.spritecollide(player, kvartalses, False):
                hits = pygame.sprite.spritecollide(cursor, kvartalses, False)
                for hit in hits:
                    alpha = random.randrange(0,100)
                    if alpha <= 10:
                        skrepka = Screpki(hit.centerx + random.randrange(int(-hit.xx/2),int(hit.xx/2)), hit.centery + random.randrange(int(-hit.yy/2),int(hit.yy/2)))
                        all_sprites.add(skrepka)
                        screpkas.add(skrepka)
                    elif alpha >= 95:
                        treat = Treats(hit.centerx + random.randrange(int(-hit.xx/2),int(hit.xx/2)), hit.centery + random.randrange(int(-hit.yy/2),int(hit.yy/2)))
                        all_sprites.add(treat)
                        treats_group.add(treat)
                    elif alpha == 75:
                        raretreat = Raretreats(hit.centerx + random.randrange(int(-hit.xx/2),int(hit.xx/2)), hit.centery + random.randrange(int(-hit.yy/2),int(hit.yy/2)))
                        all_sprites.add(raretreat)
                        raretreats_group.add(raretreat)
                #kakurzhatka  = Kakurzhatka(player.x + random.randrange(-300,300) - WIDTH/2 + 200, player.y + random.randrange(-300,300) - HEIGHT/2 + 200)
                #kakurzhatka1 = Kakurzhatka(player.x + random.randrange(-300,300) - WIDTH/2 + 200, player.y + random.randrange(-300,300) - HEIGHT/2 + 200)
                #kakurzhatka2 = Kakurzhatka(player.x + random.randrange(-300,300) - WIDTH/2 + 200, player.y + random.randrange(-300,300) - HEIGHT/2 + 200)
                #kakurzhatka3 = Kakurzhatka(player.x + random.randrange(-300,300) - WIDTH/2 + 200, player.y + random.randrange(-300,300) - HEIGHT/2 + 200)
                #kakurzhatka4 = Kakurzhatka(player.x + random.randrange(-300,300) - WIDTH/2 + 200, player.y + random.randrange(-300,300) - HEIGHT/2 + 200)
                #kakurzhatkas.add(kakurzhatka, kakurzhatka1, kakurzhatka2, kakurzhatka3, kakurzhatka4)
                #all_sprites.add(kakurzhatka, kakurzhatka1, kakurzhatka2, kakurzhatka3, kakurzhatka4)
        elif pygame.sprite.spritecollide(player, obstacles, False) and player.activity == 'run' and player.is_stay:
            player.activity = 'undumb'
            hits = pygame.sprite.spritecollide(player, obstacles, False) 
            if player.maQuests == 1:   
                for hit in hits:
                    if hit.f == 'bridge':
                        player.kyrp_num += 1
                        player.text[4] = player.text[4] = "Побиться головой об кирпичную стенку 75 раз: " + str(player.kyrp_num) + "/75"
            elif player.maQuests == 2:   
                for hit in hits:
                    if hit.f == 'bridge':
                        player.kyrp_num += 1
                        player.text[4] = player.text[4] = "Побиться головой об кирпичную стенку 150 раз: " + str(player.kyrp_num) + "/150"
            if pygame.sprite.spritecollide(cursor, kvartalses, False) or pygame.sprite.spritecollide(player, kvartalses, False):
                hits = pygame.sprite.spritecollide(player, kvartalses, False)
                for hit in hits:
                    alpha = random.randrange(0,100)
                    if alpha <= 10:
                        skrepka = Screpki(hit.centerx + random.randrange(int(-hit.xx/2),int(hit.xx/2)), hit.centery + random.randrange(int(-hit.yy/2),int(hit.yy/2)))
                        all_sprites.add(skrepka)
                        screpkas.add(skrepka)
                    elif alpha >= 95:
                        treat = Treats(hit.centerx + random.randrange(int(-hit.xx/2),int(hit.xx/2)), hit.centery + random.randrange(int(-hit.yy/2),int(hit.yy/2)))
                        all_sprites.add(treat)
                        treats_group.add(treat)
                    elif alpha == 75:
                        raretreat = Raretreats(hit.centerx + random.randrange(int(-hit.xx/2),int(hit.xx/2)), hit.centery + random.randrange(int(-hit.yy/2),int(hit.yy/2)))
                        all_sprites.add(raretreat)
                        raretreats_group.add(raretreat)
                player.kveat_num += 1
                if player.maQuests == 3:
                    player.text[4] = "Побиться головой о кирпичное здание с красной крышей 40 раз: " + str(player.kveat_num) + "/40"
                elif player.maQuests == 4:
                    player.text[4] = "Побиться головой о кирпичное здание с красной крышей 175 раз: " + str(player.kveat_num) + "/175"
        if pygame.sprite.spritecollide(cursor, kakurzhatkas, False) and player.is_stay and player.activity == 'run':
            player.kaNum += 1
            player.liquid += 0.25 * player.effect
            player.activity = 'dumb'
            if player.maQuests == 5:
                player.text[4] = "Обкукуцано какуржаток: " + str(player.kaNum) + "/15"
        elif pygame.sprite.spritecollide(player, kakurzhatkas, False) and player.activity == 'run' and player.is_stay:
            player.activity = 'undumb'
        if pygame.sprite.spritecollide(player, screpkas, True):
            player.skrepks += 1
            player.wage_num += 1
            if player.maQuests == 2:
                player.text[5] = "Накопить 50 скрепок к моменту завершения квеста: " + str(player.skrepks) + "/50"
            elif player.maQuests == 3:
                player.text[5] = "Получить 10 скрепок от довольных жителей: " + str(player.wage_num) + "/10"
            elif player.maQuests == 4:
                player.text[5] = "Получить 35 скрепок от довольных жителей: " + str(player.wage_num) + "/35"
        if pygame.sprite.spritecollide(player, treats_group, True):
            i = player.inv.get('treat', [0])[0] + 1
            player.inv['treat'] = [i, 43, 153]
            if player.maQuests == 3:
                player.treat_num += 1
                player.text[6] = "Подобрать 1 печенье: " + str(player.treat_num) + "/1"


        if pygame.sprite.spritecollide(player, raretreats_group, True):
            i = player.inv.get('raretreat', [0])[0] + 1
            player.inv['raretreat'] = [i, 153, 153]
        hits = pygame.sprite.spritecollide(player, obstacles2, False)
        fath.cadr -= 5
        for hit in hits:
            if hit.f == 'q-Fath':
                fath.cadr += 10
                if keystate[pygame.K_a]:
                    questses.q_fath_1 = True
                    try:
                        if player.quest['dumb'] <= player.beats:
                            player.faQuests += 1
                            if 0 < player.quest['dumb'] < 10:
                                player.skrepks += random.randrange(1, 3)
                            elif 15 <= player.quest['dumb'] < 35:
                                player.skrepks += random.randrange(2, 8)
                            else:
                                player.skrepks += random.randrange(6, 16)
                            if player.maQuests == 2:
                                player.text[5] = "Накопить 50 скрепок к моменту завершения квеста: " + str(player.skrepks) + "/50"
                            player.quest = {'dumb': random.randrange(0, 50)}
                            player.beats = 0
                            if player.maQuests == 5:
                                player.text[6] = "Выполнено дедовских квестов: " + str(player.faQuests) + "/10"
                    except:
                        player.quest = {'dumb': random.randrange(0, 50)}
            elif hit.f == 'shop-01' and pygame.time.get_ticks()-ticks > 500 and keystate[pygame.K_s]:
                slide = 'shop'
                ticks = pygame.time.get_ticks()
            if hit.f == 'q-Moth1':
                if keystate[pygame.K_a]:
                    if player.maQuests == 0:
                        player.maQuests += 1
                        questses.q_moth_1 = True
                        player.kyrp_num, player.sink_num = 0,0
                        player.text[3] = "Синяя Стенка (от Ржалии): " 
                        player.text[4] = "Побиться головой об кирпичную стенку 75 раз: " + str(player.kyrp_num) + "/75"
                        player.text[5] = "Купить синьку 3 раза: " + str(player.sink_num) + "/3"
                        player.text[6] = ""
                        player.text[7] = ""
                    elif player.maQuests == 1 and player.sink_num >= 3 and player.kyrp_num >= 75:
                        player.maQuests += 1
                        i = player.inv.get('40%', [0])[0] + 2
                        player.inv['40%'] = [i, 153, 43]
                        player.skrepks += 15
                        questses.q_moth_2 = True
                        player.kyrp_num = 0
                        player.text[3] = "Экономия И Экономика (от Ржалии): " 
                        player.text[4] = "Побиться головой об кирпичную стенку 150 раз: " + str(player.kyrp_num) + "/150"
                        player.text[5] = "Накопить 50 скрепок к моменту завершения квеста: " + str(player.skrepks) + "/50"
                        player.text[6] = ""
                        player.text[7] = ""
                    elif player.maQuests == 2 and player.skrepks >= 50 and player.kyrp_num >= 150:
                        player.maQuests += 1
                        i = player.inv.get('59%', [0])[0] + 1
                        player.inv['59%'] = [i, 153, 43]
                        player.skrepks += 25
                        questses.q_moth_3 = True
                        player.kveat_num = 0
                        player.wage_num = 0
                        player.treat_num = 0
                        player.text[3] = "Общественное Место (от Ржалии): " 
                        player.text[4] = "Побиться головой о кирпичное здание с красной крышей 40 раз: " + str(player.kveat_num) + "/40"
                        player.text[5] = "Получить 10 скрепок от довольных жителей: " + str(player.wage_num) + "/10"
                        player.text[6] = "Подобрать 1 печенье: " + str(player.treat_num) + "/1"
                        player.text[7] = ""
                    elif player.maQuests == 3 and player.kveat_num >= 40 and player.wage_num >= 10 and player.treat_num  >= 1:
                        player.maQuests += 1
                        player.skrepks += 40
                        i = player.inv.get('treat', [0])[0] + 1
                        player.inv['treat'] = [i, 43, 153]
                        questses.q_moth_4 = True
                        player.kveat_num = 0
                        player.wage_num = 0
                        player.treat_eat = 0
                        player.raretreat_eat = 0
                        player.text[3] = "Общественное Место 2 (от Ржалии): " 
                        player.text[4] = "Побиться головой о кирпичное здание с красной крышей 175 раз: " + str(player.kveat_num) + "/175"
                        player.text[5] = "Получить 35 скрепок от довольных жителей: " + str(player.wage_num) + "/35"
                        player.text[6] = "Употребить 15 печений: " + str(player.treat_eat) + "/15"
                        player.text[7] = "Продегустировать 3 редких печенья: " + str(player.raretreat_eat) + "/3"
                    elif player.maQuests == 4 and player.kveat_num >= 175 and player.wage_num >= 35 and player.treat_eat  >= 15 and player.raretreat_eat >= 3:
                        player.maQuests += 1
                        player.skrepks += 30
                        i = player.inv.get('raretreat', [0])[0] + 1
                        player.inv['raretreat'] = [i, 153, 153]
                        questses.q_moth_5 = True
                        player.pyrzhNum = 0
                        player.kaNum = 0
                        player.faQuests = 0
                        player.text[3] = "В погоне за пыржей (от Ржалии): " 
                        player.text[4] = "Обкукуцано какуржаток: " + str(player.kaNum) + "/15"
                        player.text[5] = "Выпито пыржанки: " + str(player.pyrzhNum) + "/5"
                        player.text[6] = "Выполнено дедовских квестов: " + str(player.faQuests) + "/10"
                        player.text[7] = ""
                    elif player.maQuests == 5 and 5 <= player.pyrzhNum and 15 <= player.kaNum and 10 <= player.faQuests:
                        player.firzt_quest_pyrzha = True
                    else:
                        questses.q_moth_0 = True
#                try:
#                    if player.quest2['pyrzhNum'] <= player.pyrzhNum and player.quest2['kaNum'] <= player.kaNum and player.quest2['faQuests'] <= player.faQuests:
#                        player.firzt_quest_pyrzha = True
#                except:
#                    player.quest2 = {'pyrzhNum': 5, 'kaNum': 15, 'faQuests': 10}
#                    player.text[3] = "В погоне за пыржей (от Ржалии): " 
#                    player.text[4] = "Обкукуцано какуржаток: " + str(player.kaNum) + "/" + str(player.quest2['kaNum'])
#                    player.text[5] = "Выпито пыржанки: " + str(player.pyrzhNum) + "/" + str(player.quest2['pyrzhNum'])
#                    player.text[6] = "Выполнено отцовских квестов: " + str(player.faQuests) + "/" + str(player.quest2['faQuests'])

        if player.isKwave == True:
            kakurzhatka  = Kakurzhatka(player.x + random.randrange(-300,300) - WIDTH/2 + 200, player.y + random.randrange(-300,300) - HEIGHT/2 + 200)
            kakurzhatka1 = Kakurzhatka(player.x + random.randrange(-300,300) - WIDTH/2 + 200, player.y + random.randrange(-300,300) - HEIGHT/2 + 200)
            kakurzhatka2 = Kakurzhatka(player.x + random.randrange(-300,300) - WIDTH/2 + 200, player.y + random.randrange(-300,300) - HEIGHT/2 + 200)
            kakurzhatka3 = Kakurzhatka(player.x + random.randrange(-300,300) - WIDTH/2 + 200, player.y + random.randrange(-300,300) - HEIGHT/2 + 200)
            kakurzhatka4 = Kakurzhatka(player.x + random.randrange(-300,300) - WIDTH/2 + 200, player.y + random.randrange(-300,300) - HEIGHT/2 + 200)
            kakurzhatkas.add(kakurzhatka, kakurzhatka1, kakurzhatka2, kakurzhatka3, kakurzhatka4)
            all_sprites.add(kakurzhatka, kakurzhatka1, kakurzhatka2, kakurzhatka3, kakurzhatka4)
            player.isKwave = False
        # Rendering
        all_sprites.draw(screen)
        obstacles.draw(screen)
        obstacles2.draw(screen)
        if questses.q_moth_0 or questses.q_moth_1 or questses.q_moth_2 or questses.q_moth_3 or questses.q_moth_4 or questses.q_moth_5 or questses.q_fath_1:
            questseses.draw(screen)
        if pygame.sprite.collide_rect(Obstacles(0,0,100,100, None), Obstacles(pos[0], pos[1], 1, 1, None)):
            try:
                unn = 75
                for i in player.text:
                    unn += 20
                    draw_text(screen, i, 18, 25, unn)
            except:
                draw_text(screen, str(player.beats), 18, 25, 25)
        else:
            try:
                draw_text(screen, str(player.beats) + "/" + str(player.quest['dumb']), 18, 25, 25)
            except:
                pass
        screpk_rect.x = 100
        screpk_rect.y = 25
        screen.blit(screpk, screpk_rect)
        draw_text(screen, str(player.skrepks), 18, 117, 25)
        # After all, turn the screen
        pygame.display.flip()
    elif slide == 'inv':
        screen.fill(GREEN)
        screen.blit(inventory_img, inventory_rect)
        pos = pygame.mouse.get_pos()
        if player.inv.get('ka_badge', None) != None and player.firzt_quest_pyrzha:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_rect(Obstacles(rect_ka_badge.x, rect_ka_badge.y, rect_ka_badge.width, rect_ka_badge.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linkerK == False:
                buttonK = True
                linkerK = True
                button = False
                button3 = False
                button2 = False
                buttonT = False
                buttonRT = False
            if event.type != pygame.MOUSEBUTTONDOWN:
                linkerK = False
            rect_ka_badge.x = WIDTH/2-510+43
            rect_ka_badge.y = HEIGHT/2-330+253
            screen.blit(img_ka_badge, rect_ka_badge)
            if buttonK == True:
                linkerK, buttonK = show_button(
                    rect_ka_badge.x-25, rect_ka_badge.y+70, pos, linkerK, buttonK, 'ka_badge')
        if player.inv.get('treat', None) != None:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_rect(Obstacles(rect_treat.x, rect_treat.y, rect_treat.width, rect_treat.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linkerT == False:
                buttonT = True
                linkerT = True
                button = False
                button2 = False
                button3 = False
                buttonK = False
                buttonRT = False
            if event.type != pygame.MOUSEBUTTONDOWN:
                linkerT = False
            rect_treat.x = WIDTH/2-510+player.inv['treat'][1]
            rect_treat.y = HEIGHT/2-330+player.inv['treat'][2]
            screen.blit(img_treat, rect_treat)
            if player.inv['treat'][0] < 100:
                draw_text(screen, 'X ' + str(player.inv['treat'][0]), 18, WIDTH/2-510+player.inv['treat'][1]+30, HEIGHT/2-330+player.inv['treat'][2]-10)
            else:
                draw_text(screen, 'X' + str(player.inv['treat'][0]), 18, WIDTH/2-510+player.inv['treat'][1]+30, HEIGHT/2-330+player.inv['treat'][2]-10)
            if buttonT == True:
                linkerT, buttonT = show_button(
                    rect_treat.x-25, rect_treat.y+70, pos, linkerT, buttonT, 'treat')
        if player.inv.get('raretreat', None) != None:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_rect(Obstacles(rect_raretreat.x, rect_raretreat.y, rect_raretreat.width, rect_raretreat.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linkerRT == False:
                buttonRT = True
                linkerRT = True
                button = False
                button2 = False
                button3 = False
                buttonK = False
                buttonT = False
            if event.type != pygame.MOUSEBUTTONDOWN:
                linkerRT = False
            rect_raretreat.x = WIDTH/2-510+player.inv['raretreat'][1]
            rect_raretreat.y = HEIGHT/2-330+player.inv['raretreat'][2]
            screen.blit(img_raretreat, rect_raretreat)
            if player.inv['raretreat'][0] < 100:
                draw_text(screen, 'X ' + str(player.inv['raretreat'][0]), 18, WIDTH/2-510+player.inv['raretreat'][1]+30, HEIGHT/2-330+player.inv['raretreat'][2]-10)
            else:
                draw_text(screen, 'X' + str(player.inv['raretreat'][0]), 18, WIDTH/2-510+player.inv['raretreat'][1]+30, HEIGHT/2-330+player.inv['raretreat'][2]-10)
            if buttonRT == True:
                linkerRT, buttonRT = show_button(
                    rect_raretreat.x-25, rect_raretreat.y+70, pos, linkerRT, buttonRT, 'raretreat')
        if player.inv.get('59%', None) != None:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_rect(Obstacles(rect59.x, rect59.y, rect59.width, rect59.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linker3 == False:
                button3 = True
                linker = True
                button2 = False
                button = False
                buttonK = False
                buttonT = False
                buttonRT = False
            if event.type != pygame.MOUSEBUTTONDOWN:
                linker3 = False
            rect59.x = WIDTH/2-510+player.inv['59%'][1]
            rect59.y = HEIGHT/2-330+player.inv['59%'][2]
            screen.blit(img59, rect59)
            draw_text(screen, 'X ' + str(player.inv['59%'][0]), 18, WIDTH /
                      2-510+player.inv['59%'][1], HEIGHT/2-330+player.inv['59%'][2]+40)
            if button3 == True:
                linker3, button3 = show_button(
                    rect59.x-25, rect59.y+70, pos, linker3, button3, '59%')
        if player.inv.get('40%', None) != None:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_rect(Obstacles(rect40.x, rect40.y, rect40.width, rect40.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linker2 == False:
                button2 = True
                linker2 = True
                button = False
                button3 = False
                buttonK = False
                buttonT = False
                buttonRT = False
            if event.type != pygame.MOUSEBUTTONDOWN:
                linker2 = False
            rect40.x = WIDTH/2-510+player.inv['40%'][1]
            rect40.y = HEIGHT/2-330+player.inv['40%'][2]
            screen.blit(img40, rect40)
            draw_text(screen, 'X ' + str(player.inv['40%'][0]), 18, WIDTH /
                      2-510+player.inv['40%'][1], HEIGHT/2-330+player.inv['40%'][2]+40)
            if button2 == True:
                linker2, button2 = show_button(
                    rect40.x-25, rect40.y+70, pos, linker2, button2, '40%')
        if player.inv.get('20%', None) != None:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.collide_rect(Obstacles(rect20.x, rect20.y, rect20.width, rect20.height, None), Obstacles(pos[0], pos[1], 1, 1, None)) and linker == False:
                button = True
                linker = True
                button2 = False
                button3 = False
                buttonK = False
                buttonT = False
                buttonRT = False
            if event.type != pygame.MOUSEBUTTONDOWN:
                linker = False
            rect20.x = WIDTH/2-510+player.inv['20%'][1]
            rect20.y = HEIGHT/2-330+player.inv['20%'][2]
            screen.blit(img20, rect20)
            draw_text(screen, 'X ' + str(player.inv['20%'][0]), 18, WIDTH /
                      2-510+player.inv['20%'][1], HEIGHT/2-330+player.inv['20%'][2]+40)
            if button == True:
                linker, button = show_button(
                    rect20.x-25, rect20.y+70, pos, linker, button, '20%')
        for event in pygame.event.get():
            # Check window's closing
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                running = False
            if keystate[pygame.K_e] and pygame.time.get_ticks()-ticks > 500:
                slide = 'game'
                ticks = pygame.time.get_ticks()
        # After all, turn the screen
        pygame.display.flip()
    elif slide == 'char':
        screen.fill(GREEN)
        screen.blit(char_img, char_rect)
        for event in pygame.event.get():
            # Check window's closing
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                running = False
            if keystate[pygame.K_q] and pygame.time.get_ticks()-ticks > 500:
                slide = 'game'
                ticks = pygame.time.get_ticks()
        player.dolb = float("{0:.2f}".format(player.dolb))
        draw_text(screen,str(float(player.dolb)),50,char_rect.x+515,char_rect.y+58,((97,97,97)),True)
        # After all, turn the screen
        pygame.display.flip()
    elif slide == 'shop':
        pos = pygame.mouse.get_pos()
        screen.fill(GREEN)
        screen.blit(shop_img, shop_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 0 < pos[1] - shop_rect.y <= 220 and 0 < pos[0] - shop_rect.x <= shop_rect.x + 1020 and player.skrepks >= 5:
                    player.skrepks -= 5
                    if player.maQuests == 2:
                        player.text[5] = "Накопить 50 скрепок к моменту завершения квеста: " + str(player.skrepks) + "/50"
                    i = player.inv.get('20%', [0])[0] + 1
                    player.inv['20%'] = [i, 43, 43]
                elif 220 < pos[1] - shop_rect.y <= 440 and 0 < pos[0] - shop_rect.x <= 1020 and player.skrepks >= 15:
                    player.skrepks -= 15
                    if player.maQuests == 2:
                        player.text[5] = "Накопить 50 скрепок к моменту завершения квеста: " + str(player.skrepks) + "/50"
                    i = player.inv.get('40%', [0])[0] + 1
                    player.inv['40%'] = [i, 153, 43]
                    player.sink_num += 1
                    player.sink_num = min(player.sink_num, 3)
                    if player.maQuests == 1:
                        player.text[5] = "Купить синьку 3 раза: " + str(player.sink_num) + "/3"
                elif 440 < pos[1] - shop_rect.y <= 660 and 0 < pos[0] - shop_rect.x <= 1020 and player.skrepks >= 100:
                    player.skrepks -= 100
                    if player.maQuests == 2:
                        player.text[5] = "Накопить 50 скрепок к моменту завершения квеста: " + str(player.skrepks) + "/50"
                    i = player.inv.get('59%', [0])[0] + 1
                    player.inv['59%'] = [i, 263, 43]   
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_ESCAPE]:
                running = False 
            elif keystate[pygame.K_s] and pygame.time.get_ticks()-ticks > 500:
                slide = 'game'
                ticks = pygame.time.get_ticks()          
        pygame.display.flip()
    else:
        print("EROOR")
with open(save, 'w') as file:
    if player.liquid > 0:
        file.write(str(player.skrepks)+'\n')
        file.write(str(player.x)+'\n')
        file.write(str(player.y)+'\n')
        file.write(str(player.liquid)+'\n')
        file.write(str(player.tired)+'\n')
        file.write(' '.join([str(i) for i in camera]) + '\n')
        file.write(str(player.inv.get('20%', [0])[0]) + ' ' + str(player.inv.get('40%', [0])[0]) + ' ' + str(player.inv.get('59%', [0])[0])  + ' 43 153 263 43 43 43' + '\n')
        file.write(str(player.maximum)+'\n')
        file.write(str(player.effect)+'\n')
        file.write(str(player.thirst)+'\n')
        file.write(str(player.beats) + ' ' + str(player.quest['dumb']) + '\n')
        player.dolb = float("{0:.2f}".format(player.dolb))
        file.write(str(player.dolb) + "\n")
        file.write(str(int(player.kaNum)) + " " + str(int(player.pyrzhNum)) + " " + str(int(player.faQuests)) + '\n')
        file.write(str(int(player.firzt_quest_pyrzha)) + '\n')
        file.write(str(player.inv.get('treat', [0])[0]) + ' 43 153\n')
        file.write(str(player.inv.get('raretreat', [0])[0]) + ' 153 153\n')
        file.write(str(player.health)+'\n')
        file.write(str(player.maQuests)+'\n')
        if player.maQuests == 1:
            file.write(str(player.kyrp_num) + ' ' + str(player.sink_num) + '\n')
        elif player.maQuests == 2:
            file.write(str(player.kyrp_num) + '\n')
        elif player.maQuests == 3:
            file.write(str(player.kveat_num) + ' ' + str(player.wage_num) + ' ' + str(player.treat_num) + '\n')
        elif player.maQuests == 4:
            file.write(str(player.kveat_num) + ' ' + str(player.wage_num) + ' ' + str(player.treat_eat) + ' ' + str(player.raretreat_eat) + '\n')
    else:
        pass
pygame.quit()