import pygame
from random import randint
pygame.init()
FPS = 60
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

run = True
x = 50
y = 50
y1 = 150
x1 = 50
x2 = 780
y2 = 0
road = []
direction = "stop"
bmw = pygame.image.load("zelda.png")
for i in range(10, WIDTH, 100):
    road.append([i, 115, 35, 10])
while run:
    window.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                direction = "left"
            if i.key == pygame.K_RIGHT:
                direction = "right"
            if i.key == pygame.K_UP:
                direction = "up"
            if i.key == pygame.K_DOWN:
                direction = "down"
        elif i.type == pygame.KEYUP:
            direction = "stop"
    if direction == "left" and x > 0:
        x -= 3
    if direction == "right" and x < WIDTH - 70:
        x += 3
    if direction == "up" and y > 0:
        y -= 3
    if direction == "down" and y < HEIGHT - 30:
        y += 3

    window.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.blit(bmw,(x,y))
























    pygame.display.update()
    clock.tick(FPS)
pygame.quit()