import pygame, time, random
pygame.init()
def Game_Start(gg):
    gg==gg
    from pygame.color import THECOLORS
    screen=pygame.display.set_mode([640,480])
    screen.fill([0,0,0])
    r=20
    x=0
    y=150
    dx=3
    dy=3
    xr=0
    yr=190
    dd=620
    ss=190
    heigth=150
    width=20
    k=0
    h=0
    running = True
    step=3
    while running:
        screen.fill([0,0,0])
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
        if yr>=480-145:
            yr-=step
        if yr<=0:
            yr+=step
        font = pygame.font.Font(None,35)
        text = font.render(" "+ str (k),1,THECOLORS['blue'])
        screen.blit(text,[330,20])
        font = pygame.font.Font(None,35)
        text = font.render(" "+ str (h),1,THECOLORS['blue'])
        screen.blit(text,[280,20])
        pygame.draw.rect(screen,THECOLORS['white'] , [318, 0, 2,480], 0)
        pygame.draw.circle(screen,THECOLORS['white'] , [320, 245],100, 5) 
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
            k+=1
        if (x<=50) and yr<y<yr+heigth:
            dx=2
        if (x>=590) and ss<y<ss+heigth:
            dx=-2
        if x>=640:
            x=320
            h+=1
        if k==5:
            from main import main
            quit()
        if h==5:
            from main import main
            quit()
        else:
            pygame.time.delay(10)
            pygame.display.flip()  
    pygame.quit()




