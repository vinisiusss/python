
import pygame, random
pygame.init()
from pygame import font
from pygame.color import THECOLORS
screenX = 500
screenY = 500
screen = pygame.display.set_mode([screenX, screenY])
n_str=10
n_stolb=10
h=50
tab=[0]*n_stolb
for i in range(n_str):
    tab[i]=[0]*n_stolb
pole=[0]*n_stolb
for i in range(n_str):
    pole[i]=[0]*n_stolb
lab=open('lab2.txt','r')
for i in range(n_str):
    lines=lab.readline()
    s=lines.split()
    for j in range(n_stolb):
        tab[i][j]=int(s[j])
lab.close()
nx=25
ny=25
tree= pygame.image.load("22.png")
tree.set_colorkey((255, 255, 255))
hero= pygame.image.load("33.png")
hero.set_colorkey((255, 255, 255))
vrag= pygame.image.load("44.png")
vrag.set_colorkey((255, 255, 255))
priz1= pygame.image.load("1234.png")
priz1.set_colorkey((255, 255, 255))
priz2= pygame.image.load("gyu.png")
priz2.set_colorkey((255, 255, 255))
priz3= pygame.image.load("guy.png")
priz3.set_colorkey((255, 255, 255))
n_priz=0
j_vrag=[]
i_vrag=[]
j_hero=[]
i_hero=[]
x=0
y=0
def drawlab(i_hero,j_hero,i_vrag,j_vrag, n_priz):
    for i in range(n_str):
        for j in range(n_stolb):
            x=nx+j*h-40
            y=ny+i*h-40
            if tab[i][j]==1:
                screen.blit(tree,[x,y])
            elif tab[i][j]==2:
                screen.blit(hero,[x,y])
                i_hero=i
                j_hero=j
                tab[i][j]=0
            elif tab[i][j]==3:
                screen.blit(vrag,[x,y])
                i_vrag=i
                j_vrag=j
            elif tab[i][j]==4:
                screen.blit(priz1,[x,y])
                n_priz+=1
            elif tab[i][j]==5:
                screen.blit(priz2,[x,y])
                n_priz+=1
            elif tab[i][j]==6:
                screen.blit(priz3,[x,y])
                n_priz+=1
    return i_hero,j_hero,i_vrag,j_vrag,n_priz
drawlab(i_hero,j_hero,i_vrag,j_vrag, n_priz)
for i in range(n_str):
        for j in range(n_stolb):
            stepi=i
            stepj=j
            def hodit (i_hero,j_hero,stepi,stepj):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            i_hero=i_hero-stepi
                        elif event.key == pygame.K_DOWN:
                            i_hero=i_hero+stepi
                        elif event.key == pygame.K_LEFT:
                             j_hero=j_hero-stepj
                        elif event.key == pygame.K_RIGHT:
                             j_hero=j_hero+stepj
                delay=100
                interval=10
                return i_hero,j_hero,stepi,stepj
hodit(i_hero,j_hero,stepi,stepj)
running = True
running=True
while running:
    hodit(i_hero,j_hero,stepi,stepj)
    pygame.time.delay(50)
    pygame.display.flip()
pygame.quit()





