import pygame,random,time
pygame.init()
screen=pygame.display.set_mode([800,800])
r=20
xc=200
yc=300
dx=0
dy=4
k=0
k1=0
click=False


running=True
while running:
    screen.fill([255,240,251])
    pygame.draw.circle(screen,[100,100,50],[xc,yc],r,0)

    dx=random.randint(0,1)
    if dx ==0:
        dy=random.randint(-10,10)
    elif dx==1:
        dx=random.randint(-10,10)
        dy=0
        
    if xc <=r+r:
        dx=30
    if xc >=800-r-r:
        dx=-30
    if yc>=800-r-r:
        dy=-30
    if yc<=r+r:
        dy=30
        
    xc=xc+dx
    yc=yc+dy
    
    x=64
    h=100
    
    font = pygame.font.Font(None,35)
    text = font.render("Выстрелы: "+ str(k),1,[0,0,0])
    screen.blit(text,[550,700])

    font = pygame.font.Font(None,35)
    text = font.render('Попадания: '+str(k1),1,[0,0,0])
    screen.blit(text,[550,750])
    

    pygame.time.delay(12)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = True
            (x1,y1) = event.pos
            k=k+1
            if ((xc-x1)**2+(yc-y1)**2)<=r**2:
                k1=k1+1
                screen.fill([255,240,251])
                xc=random.randint(20,780)
                yc=random.randint(20,780)
        elif event.type == pygame.MOUSEBUTTONUP:
            click = False
pygame.quit()
