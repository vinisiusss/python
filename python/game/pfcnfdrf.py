import pygame, time, random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 560
HEIGHT = 720
FPS = 60
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("egor_lox")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text (surf, text, size, x, y, COLOR):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, COLOR)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inac_color = (255, 255, 255)
        self.act_color = (0, 40, 40)

    def draw(self, x, y, text, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x +self.width and y < mouse[1] < y +self.height:
            pygame.draw.rect(screen, self.act_color, (x, y, self.width, self.height))

            if click[0] == 1 and action is not None:
                time.sleep(0.1)
                action()
                if action == quit:
                    pygame.quit()
                    quit()
                    

        else:
            pygame.draw.rect(screen, self.inac_color, (x, y, self.width, self.height))
        draw_text(screen, text, 25, x + 55, y + 15, BLACK)
def menu():
    start_btn = Button(250, 65)
    help_btn = Button(250, 65)
    dev_btn = Button(250, 65)
    ex_btn = Button(250, 65)
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(BLACK)
        start_btn.draw(160, 270, "         Начать игру", None)
        ex_btn.draw(160, 350, "Выход", quit)
        pygame.display.update()
        clock.tick(FPS)


menu()
