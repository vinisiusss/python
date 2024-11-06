import pygame, time, random
pygame.init()
from pygame.color import THECOLORS
screenX=500
screenY=500
screen=pygame.display.set_mode([screenX,screenY])
screen.fill([255,255,255] )
frukt=[] # Массив поверхностей с рисунками фруктов
fr_scr=[] # логический массив: True – падает, False – фрукта нет, он пойман
popal=False # Признак поимки фрукта
sm=0 # Счетчик пойманных фруктов
n=3
dy=[]
step=40
x=[]
y=[]
x_korz=250
y_korz=400
run=True
n_file=["еда11.png","еда21.jpg","еда31.jpg"]
korz=pygame.image.load("корзинка.jpg")
for j in range (n):
    fr=pygame.image.load(n_file[j])  
    frukt+=[fr]
    fr_scr+=[True]
    x+= [random.randint(0,screenX-32)]
    y+= [0]
    dy+=[random.randint(2,10)]
while run==True:
    for j in range (n):
            pygame.draw.rect(screen,THECOLORS['white'], [0, 0, 150, 100], 0)
            font = pygame.font.Font(None, 45) #задаем шрифт, 45 - размер шрифта
            text1 = font.render(" Очки "+str(sm),True, [0,0,255])
            screen.blit(text1, [10, 40])
            screen.blit(korz, [x_korz,y_korz])
            pygame.display.flip()
            if fr_scr[j]: # Если фрукт еще не пойман
                pygame.draw.rect(screen,THECOLORS['white'], [x[j], y[j], 90, 50], 0)
                y[j]=y[j]+dy[j]
                screen.blit(frukt[j], [x[j],y[j]])
                pygame.display.flip()
            if (y[j]>=screenY):
              # Появляется вверху новый рисунок
                x[j]=random.randint(0,screenX-32)
                y[j]=0
                dy[j]=random.randint(2,10)
                pygame.draw.rect(screen,THECOLORS['white'], [x[j], y[j], 90, 50], 0)
                screen.blit(frukt[j], [x[j],y[j]])
            if sm==n:
                text = font.render('Вы победили',True, [0,0,255])
                screen.blit(text, [290, 40])
                pygame.display.flip()
                pygame.time.delay(4000)
                run= False
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    run= False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        pygame.draw.rect(screen,THECOLORS['white'], [x_korz,y_korz, 120, 100], 0)
                        x_korz=x_korz+step
                    elif event.key == pygame.K_LEFT:
                        pygame.draw.rect(screen,THECOLORS['white'], [x_korz,y_korz, 120, 100], 0)
                        x_korz-=step
                        
                    if x_korz>=400:
                        x_korz=400
                    if x_korz<=0-20:
                        x_korz+=step
            if(x[j]>=x_korz)and(x[j]+40<=x_korz+100)and(y[j]>=y_korz-40):
                x[j]=random.randint(0,screenX-32)
                y[j]=0
                dy[j]=random.randint(2,10)
                sm=sm+1 #Подчет очков
                screen.fill([255,255,255] )
                screen.blit(frukt[j], [x[j],y[j]])
                pygame.display.flip()

            pygame.time.delay(10)# задержка на 10 миллисекунд
            
            
pygame.quit()           
