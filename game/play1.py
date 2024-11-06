import pygame, time, random, sys
pygame.init()
from pygame.color import THECOLORS
screen=pygame.display.set_mode([640,480])
screen.fill([0,0,0])
r=20
x=0
y=150
dx=4
dy=4
xr=0
yr=350
heigth=150
width=20
h=0
step=5
sped=3
running = True
while running:
    screen.fill([0,0,0])
    font = pygame.font.Font(None,35)
    text = font.render("количество отбиваний "+ str (h),1,THECOLORS['blue'])
    screen.blit(text,[280,20])
    pygame.draw.rect(screen,THECOLORS['green'] , [xr, yr, width, heigth], 0)
    x=x+dx
    y=y+dy
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_s]:
        yr=yr+step
    if keys[pygame.K_w]:
        yr=yr-step 
    if yr>=640-300:
        yr-=step
    if yr<=0:
        yr+=step  
    pygame.draw.circle(screen,THECOLORS['red'],[x,y],r,0)
    if h>=3:
        sped=5
    if h>=10:
        sped=8
    if (y>=480-r):
        dy=-sped
    if y<0+r:
        dy=sped
    if (x<=50) and yr<y<yr+heigth:
        dx=sped
    if (x==50) and yr<y<yr+heigth:
        h+=1
    if (x>=640-r):
        dx=-sped
    if x<=0:
        from main import main
    else:
        pygame.time.delay(10)
        pygame.display.flip()
pygame.draw.rect(screen,THECOLORS['green'] , [600, 20, 100,10], 0)  
pygame.quit()





