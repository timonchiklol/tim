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






























    pygame.display.update()
    clock.tick(FPS)
pygame.quit()