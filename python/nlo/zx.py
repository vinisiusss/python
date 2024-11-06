import pygame, random
pygame.init()
screenX=900
screenY=600
screen = pygame.display.set_mode([screenX,screenY])
screen.fill([0,0,0]) # black
x=10
y= random.randint(10, screenY - 59)
nlo.png = pygame.image.load("nlo.png")      # загрузка рисунка из файла 
screen.blit(nlo, [x, y])                     # вывод на экран
pygame.display.flip()
running = True
while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
pygame.quit()
