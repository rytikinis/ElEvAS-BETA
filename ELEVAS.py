import pygame
import sys
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

#Music

# pygame.mixer.music.load('Crepuscular Rays.wav')
# pygame.mixer.music.play(-1)

#Veriables

font = pygame.font.SysFont('Arial', 30)
in_ = 'menu'

#Winodw

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ELEVAS')
pygame.display.set_icon(pygame.image.load('ElEvAS.png'))

#Menu

class menu():
    class elevas():
        def __init__(self):
            self.elevas = pygame.image.load('ElEvAS.png')
        def loop(self):
            global in_
            key = pygame.key.get_pressed()
            win.blit((self.elevas), (0, 0))
            if key[pygame.K_SPACE]:
                in_ = 'simulator'
#ELEVAS

class elevas():
    class stars():
        def __init__(self):
            self.num = int()
            self.blue = pygame.image.load('elevas_blue.png')
            self.red = pygame.image.load('elevas_red.png')
            self.yellow = pygame.image.load('elevas_yellow.png')
            self.white = pygame.image.load('elevas_white.png')
            self.nova = pygame.image.load('supernova.png')
            self.exploding = [pygame.image.load('SN0.png'), pygame.image.load('SN1.png'), pygame.image.load('supernova.png')]
            self.x = list()
            self.y = list()
            self.starded = list()
            self.staraleve = list()
            self.color = list()
            for a in range(20):
                if random.randint(1, 3) == 1:
                    self.color.append('blue')
                    self.starded.append(random.randint(10, 30))
                else:
                    self.color.append('yellow')
                    self.starded.append(random.randint(1000, 10000))
        def loop(self):
            key = pygame.key.get_pressed()
            self.num = 0
            for a in range(len(self.x)):
                if not self.starded[a] < time.num - 6: self.num += 1
            if self.color:
                for a in range(len(self.x)):
                    if self.starded[a] < time.num and not self.starded[a] < time.num - 2 and self.staraleve[a] < time.num:
                        win.blit(pygame.transform.scale(self.red, (70, 70)), (self.x[a] - 20, self.y[a] - 10))
                    elif self.color[a] == 'yellow':
                        if self.starded[a] < time.num:
                            win.blit(pygame.transform.scale(self.white, (10, 10)), (self.x[a] - 5, self.y[a] - 15))
                    elif self.color[a] == 'blue':
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 5 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.exploding[2], (30, 30)), (self.x[a] - 15, self.y[a] - 15))
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 4 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.exploding[1], (30, 30)), (self.x[a] - 15, self.y[a] - 15))
                        if self.starded[a] < time.num and not self.starded[a] < time.num - 3 and self.staraleve[a] < time.num:
                            win.blit(pygame.transform.scale(self.exploding[0], (30, 30)), (self.x[a] - 15, self.y[a] - 15))
                    if not self.starded[a] < time.num and self.staraleve[a] < time.num:
                        if self.color[a] == 'blue':
                            win.blit(pygame.transform.scale(self.blue, (20, 20)), (self.x[a], self.y[a]))
                        elif self.color[a] == 'yellow':
                            win.blit(pygame.transform.scale(self.yellow, (10, 10)), (self.x[a], self.y[a]))
            if self.num < 150:
                if key[pygame.K_RIGHT]:
                    if random.randint(1, 10) == 1:
                        if random.randint(1, 3) == 1:
                            self.color.append('blue')
                            self.starded.append(random.randint(round(time.num) + 10, round(time.num) + 30))
                        else:
                            self.color.append('yellow')
                            self.starded.append(random.randint(round(time.num) + 1000, round(time.num) + 10000))
                        self.x.append(random.randint(0, 800))
                        self.y.append(random.randint(0, 600))
                        self.staraleve.append(time.num)
                else:
                    if random.randint(1, 100) == 1:
                        if random.randint(1, 3) == 1:
                            self.color.append('blue')
                            self.starded.append(random.randint(round(time.num) + 10, round(time.num) + 30))
                        else:
                            self.color.append('yellow')
                            self.starded.append(random.randint(round(time.num) + 1000, round(time.num) + 10000))
                        self.x.append(random.randint(0, 800))
                        self.y.append(random.randint(0, 600))
                        self.staraleve.append(time.num)
    class time():
        def __init__(self):
            self.num = 0
        def loop(self):
            key = pygame.key.get_pressed()
            self.text = font.render(str(round(self.num)) + ' Mry ' + str(stars.num), False, (255, 255, 255))
            win.blit((self.text), (20, 20))
            if key[pygame.K_RIGHT]:
                self.num += 0.3
            else:
                self.num += 0.003
        
#Sprites

stars = elevas.stars()
time = elevas.time()
menuimg = menu.elevas()

#Loop

while True:
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if in_ == 'simulator':
        stars.loop()
        time.loop()
    else:
        menuimg.loop()
    pygame.display.update()