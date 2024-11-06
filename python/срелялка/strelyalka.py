import pygame, random
pygame.init()
from pygame import font
from pygame.color import THECOLORS
screenX = 900
screenY = 600
screen = pygame.display.set_mode([screenX, screenY])
font=pygame.font.Font(None,38)
font1 = pygame.font.Font(None, 100) 
text1= font1.render(("win"),1, THECOLORS ["black"])
nlo= pygame.image.load("нло.png")
nlo.set_colorkey((255, 255, 255))

kor=pygame.image.load("пушка.png")
kor.set_colorkey((255, 255, 255))
nebo=pygame.image.load("ggg.jpg")
raketa=pygame.image.load("пуля.png")
raketa.set_colorkey((255, 255, 255))
x_kor=screenX//2-30
y_kor=screenY-90
step=3
kolvo=0
pusk=[]
n_r=30
dyp=5
xr=[]
yr=[]
for i in range(n_r):
    pusk+=[False]
    xr.append(0)
    yr.append(0)
n=10
x=[]
y=[]
dx=[]
nlo_scr=[]
def initdata(x,y,dx,nlo_scr):
    for j in range (n):
        nlo_scr+=[True]
        x+=[random.randint(0,screenX-60)]
        y+=[random.randint(0,screenY//2+40)]
        dx+=[random.randint(-15,15)]
    return (x,y,dx,nlo_scr)
initdata(x,y,dx,nlo_scr)
for j in range(n):
    while dx[j]==0:
        dx[j]=[random.randint(-15,15)]
def move_to_horisont(x,y,dx,nlo_scr):
    if nlo_scr:
        x+=dx
        screen.blit(nlo,[x,y])
        if (x+250>=screenX-dx) or (x<-50):
            dx=-dx
    return (x,y,dx,nlo_scr)
def polet(x,y,vystrel):
    y=y-dyp
    screen.blit(raketa,[x,y])
    if y<0:
        vystrel=False
    return(x,y,vystrel)
def proverka(xr1,yr1,xn,yn,bb):
    if (xn<=xr1) and (xr1<=xn+150) and (yn<=yr1) and (yr1<=yn+80):
        bb=True
    else:
        bb=False
    return(xr1,yr1,xn,yn,bb)
def schet(kolvo):
    pygame.draw.rect(screen,[255,255,255],[screenX-135,10,133,40],0)
    tt=font.render("СБИТО "+str(kolvo),True,[0,0,0])
    return(tt)
popal=False
screen.blit(nebo,[0,0])
screen.blit(kor,[x_kor,y_kor])
for j in range(n):
    if nlo_scr[j]:
        screen.blit(nlo,[x[j],y[j]])
delay=250
interval=10
pygame.key.set_repeat(delay,interval)
k=0
running=True
while running:
    screen.blit(nebo,[0,0])
    screen.blit(kor,[x_kor,y_kor])
    tt=schet(kolvo)
    screen.blit(tt,[screenX-130,20])
    for j in range (n):
        if nlo_scr[j]:
            x[j],y[j],dx[j],nlo_scr[j]=move_to_horisont(x[j],y[j],dx[j],nlo_scr[j])
            screen.blit(nlo,[x[j],y[j]])
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                if (x_kor>=step):
                    x_kor=x_kor-step
            elif event.key==pygame.K_RIGHT:
                if(x_kor+60<=screenX-step):
                    x_kor=x_kor+step
            elif event.key == 27:
                running=False
            elif event.key == pygame.K_SPACE:
                if k<=n_r:
                    pusk[k]=True
                    xr[k]=x_kor+30
                    yr[k]=y_kor
                    screen.blit(raketa,[xr[k],yr[k]])
                    k=k+1
                    if k==n_r:
                        k=0
    for j in range(n):
        if nlo_scr[j]:
            for i in range(n_r):
                if pusk[i]:
                    xr[i],yr[i],x[j],y[j],popal=proverka(xr[i],yr[i],x[j],y[j],popal)
                    if popal:
                        nlo_scr[j]=False
                        pusk[i]=False
                        kolvo+=1
    for i in range(n_r):
        if pusk[i]:
            xr[i],yr[i],pusk[i]=polet(xr[i],yr[i],pusk[i])
    if kolvo==n:
        screen.fill([255,255,255])
        screen.blit(text1, [150, 200])
    pygame.time.delay(2)
    pygame.display.flip()
game.quit()
