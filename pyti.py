import pygame
import random
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Cabeza:
    def __init__(self, screen ,color,x,y):
        self.screen = screen
        self.color = color
        self.l = 30
        self.x = x
        self.y = y
        self.dx = 0
        self.previous_inst = "0x"
    def create(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.l, self.l))
    def move(self,inst):
        if inst[-1] == "y":
            self.y += int(inst[:-1])
        else:
            self.x += int((inst[:-1]))
        self.current_inst = inst
# class Food(Cabeza):
#     def __init__(self, screen, color,x,y):
#         super().__init__(screen,color,x,y)
#         self.x = x
#         self.y = y
#         self.l = 10

class Food:
    def __init__(self, screen):
        self.screen = screen
        self.color = (150,230,250)
        self.l = 10
        self.x = 250
        self.y = 250
    def create(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.l, self.l))
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((900,600))
food = Food(screen)
pygame.display.set_caption("Juego")
bodylist = []
bodylist.append(Cabeza(screen, GREEN,60,0))
move = "0x"
run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move = "30y"
            if event.key == pygame.K_UP:
                move = "-30y"
            if event.key == pygame.K_LEFT:
                move = "-30x"
            if event.key == pygame.K_RIGHT:
                move = "30x"
            if event.key == pygame.K_a:
                food.y = random.randint(0,600)
                food.x = random.randint(0,900)
    screen.fill(WHITE)
    for g in range(len(bodylist)):
        bodylist[g].create()
    bodylist[0].move(move)
    for k in range(1,len(bodylist)):
        bodylist[k].move(bodylist[k-1].previous_inst)
        bodylist[k-1].previous_inst = bodylist[k-1].current_inst
    food.create()
    pygame.display.flip()
    clock.tick(10)
pygame.quit()