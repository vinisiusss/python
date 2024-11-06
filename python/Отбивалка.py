
import pygame, time, random
pygame.init()
from pygame.color import THECOLORS
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])
r=20
x=0
y=20
dx=-2
dy=-1
xr=20
yr=440
width=150
heigth=30
pygame.draw.circle(screen,THECOLORS['red'],[x,y],r,0)
running = True
step=10
pygame.draw.rect(screen,THECOLORS['green'] , [xr, 20, yr,10], 0)
while running:
    screen.fill([255,255,255] )
    pygame.draw.rect(screen,THECOLORS['green'] , [xr, 20, width,10], 0)
    x=x+dx
    y=y+dy
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                xr=xr+step
            elif event.key == pygame.K_LEFT:
                xr-=step
            if xr>=640-150:
                xr-=step
            if xr<=0:
                xr+=step
    pygame.draw.circle(screen,THECOLORS['red'],[x,y],r,0)
    if (x<=0+r):
        dx=2
    if (y>=480-r):
        dy=-2
    if (y<=50) and xr<x<xr+150:
        dy=+2
    
    if y<0:
        y=450
    if (x>=640-r):
        dx=-2
    else:
        pygame.time.delay(10)
        pygame.display.flip()
    
pygame.quit()
