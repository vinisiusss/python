import pygame, sys
from pygame.color import THECOLORS
pygame.init()
window = [400, 600]
screen = pygame.display.set_mode(window)
background = pygame.Surface(screen.get_size())
pygame.display.set_caption('Игра')
my_font = pygame.font.SysFont('arial', 28)
menu_list = ['играть ', 'помощь',  'отбивалка', 'выход']
x = 100
wight = 200
height = 80
y = [60, 160, 260, 360, 460]
run = True
j = 5
while run:
    background.fill(THECOLORS['red'])
    for i in range(4):
        pygame.draw.rect(background,(184, 202, 255), [x, y[i], wight, height], 0, 0)
        text = my_font.render(menu_list[i], True, THECOLORS['red'])
        background.blit(text, [x+20, y[i]+25])
    text = my_font.render('Menu', True, (184, 202, 255))
    background.blit(text, [150,10])
    screen.blit(background, [0,0])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xm, ym = pygame.mouse.get_pos()
            i = 0
            for i in range(4):
                if ((xm > x) and (xm < x + wight) and (ym > y[i]) and (ym < y[i] + height)):
                    i = i
                    break
                else:
                    i = 3
            if i == 0:
                from game import Game_Start
                Game_Start(True)
            elif i == 0:
                from game import Game_Start
                Game_Start(False)
            elif i == 1:
                from помощь import помощь
                помощь()
            elif i == 2:
                from play1 import play1
                отбивалка()
            elif i == 3:
                exit()
            

