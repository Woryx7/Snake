import pygame
import random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Introduce the  snake basic building node
class Node:
    bodylist = []

    def __init__(self, screen, color, x, y):
        self.screen = screen
        self.color = color
        self.l = 30
        self.x = x
        self.y = y
        self.dx = 0
        self.previous_inst = "0x"
        Node.bodylist.append(self)

    def create(self):
        self.rect = pygame.Rect(self.x, self.y, self.l, self.l)
        pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self, inst):
        if inst[-1] == "y":
            self.y += int(inst[:-1])
        else:
            self.x += int((inst[:-1]))
        self.current_inst = inst

#Introduce the food class
class Food:
    def __init__(self, screen):
        self.screen = screen
        self.color = (150, 230, 250)
        self.l = 10

    def pos(self):
        self.x = random.randint(0, 900)
        self.y = random.randint(0, 600)

    def create(self):
        self.rect = pygame.Rect(self.x, self.y, self.l, self.l)
        pygame.draw.rect(self.screen, self.color, self.rect)

#Initialize pygame, clock and screen
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Juego")
#Create a food object, and define its position
food = Food(screen)
food.pos()
#Initialize the head of the snake and the current movement instructions
Node(screen, GREEN, 60, 0)
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
    #Set the screem canvas
    screen.fill(WHITE)
    #Display the food and the snake nodes into the canvas
    food.create()
    for g in range(len(Node.bodylist)):
        Node.bodylist[g].create()
    #Move the snakes head with its current instruction
    Node.bodylist[0].move(move)
    #Set the nodes to follow the snakes head trail
    for k in range(1, len(Node.bodylist)):
        Node.bodylist[k].move(Node.bodylist[k - 1].previous_inst)
        Node.bodylist[k - 1].previous_inst = Node.bodylist[k - 1].current_inst
    #Set the collision instructions to add a node and recalculate the food position
    if Node.bodylist[0].rect.colliderect(food.rect):
        Node(screen, RED, Node.bodylist[-1].x, Node.bodylist[-1].y)
        food.pos()
    #Flip the canvas to show to the screen
    pygame.display.flip()
    #Introduce the refresh rate velocity
    clock.tick(10)
pygame.quit()
