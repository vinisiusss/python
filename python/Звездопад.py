import pygame, random
pygame.init()
from pygame.color import THECOLORS
screenX=900
screenY=600
screen = pygame.display.set_mode([screenX,screenY])
screen.fill([0,0,0]) # black
r=20
x = [ ] # Создаем массивы
y = [ ]
dx = [ ]
dy = [ ]
col=[ ]
size=[]
n=40
for j in range (n): # Заполняем массивы
    y+= [0]
    x+=[random.randint(0,900)] # здесь шаги могут равняться нулю
    dy+=[random.randint(1,10)]
    size+=[random.randint(50,100)]
    R=random.randint(40,255)
    G=random.randint(40,255)
    B=random.randint(40,255)
    col+=[[R,G,B]]
# Нарисуем все 15 шариков друг на друге (начальное положение)
for j in range (n):  
    font = pygame.font.Font(None, 50)
    text = font.render("*",1,col[j])
    screen.blit(text, [200, 400])
    text.fill(THECOLORS ['black'])
running = True
while running:
    screen.fill([0,0,0])
    for j in range (n):
        y[j]=y[j]+dy[j]
        font = pygame.font.Font(None,
                                size[j])
        text = font.render("*",1,col[j])
        screen.blit(text, [x[j], y[j]])
        text.fill(THECOLORS ['black'])
        if (y[j]+r>=screenY):
            y[j]=0
    pygame.time.delay(10)# задержка на 10 миллисекунд
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
pygame.quit()
