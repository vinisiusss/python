import pygame
from pygame.color import THECOLORS
pygame.init()
def помощь():
    screen = pygame.display.set_mode([600,600])
    background = pygame.Surface(screen.get_size())
    pygame.display.set_caption('Помощь')
    background.fill((184, 202, 255))
    x = 20
    y = 10
    my_font = pygame.font.SysFont('arial', 20)
    help_file = open('помощь.txt', 'r', encoding="utf-8")
    lines = help_file.readlines()
    help_file.close()
    for i in range(len(lines)):
        str = lines[i]
        str = str.rstrip()
        text = my_font.render(str, True, THECOLORS['black'])
        background.blit(text, [x, y])
        y += 20
    text = my_font.render('Нажмите esc для выхода', True, THECOLORS['red'])
    background.blit(text, [x, y+50])
    screen.blit(background, [0,0])
    pygame.display.update()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT or event.type==pygame.KEYDOWN:
                run=False
                screen=pygame.display.set_mode([400,600])
    

    #quit()
