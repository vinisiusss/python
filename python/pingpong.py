import pygame, time, random
pygame.init()
from pygame.color import THECOLORS
screen=pygame.display.set_mode([640,480])
screen.fill([0,0,0])
fps=300
r=20
x=0
y=150
dx=1
dy=1
xr=0
yr=190
dd=620
ss=190
heigth=150
width=20
pygame.draw.circle(screen,THECOLORS['red'],[x,y],r,0)
running = True
step=5
while running:
    screen.fill([0,0,0])
    pygame.draw.rect(screen,THECOLORS['green'] , [xr, yr, width, heigth], 0)
    x=x+dx
    y=y+dy
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            yr=yr-step
        elif event.key == pygame.K_DOWN:
            yr=yr+step
        if yr>=480-145:
            yr-=step
        if yr<=0:
            yr+=step
    pygame.draw.rect(screen,THECOLORS['green'] , [dd, ss,width,heigth], 0)
    x=x+dx
    y=y+dy
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            ss=ss-step
        elif event.key == pygame.K_DOWN:
            ss=ss+step
        if ss>=480-145:
            ss-=step
        if ss<=0:
            ss+=step
    pygame.draw.circle(screen,THECOLORS['red'],[x,y],r,0)
    if (y>=480-r):
        dy=-2
    if y<0+r:
        dy=+2
    if x<=0:
        x=320
    if (x<=50) and yr<y<yr+heigth:
        dx=2
    if x>=640:
        x=320
    if (x>=590) and yr<y<yr+heigth:
        dx=-dx
    else:
        pygame.time.delay(10)
        
        pygame.display.flip()
pygame.draw.rect(screen,THECOLORS['green'] , [600, 20, 100,10], 0)  
pygame.quit()




