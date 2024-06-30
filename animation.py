import pygame

pygame.init()
FPS = 60
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

run = True
x = 50
y = 50
d = "right"
while run:
    window.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.circle(window,RED,(x,y),40)
    if d == "right":
        x += 2
        y += 2
        if y == HEIGHT - 40:
            d = "left"
    if d == "left":
        x -= 2
        y -= 2
        if x == 40:
            d = "right"






























    pygame.display.update()
    clock.tick(FPS)
pygame.quit()