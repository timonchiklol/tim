import random
import mysql.connector
import pygame
from random import randint
from config import db
pygame.init()
FPS = 60
WIDTH = 800
HEIGHT = 250
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
dbconfig = {'db'}
run = True
x = 50
y = 50
y1 = 150
x1 = 50
x2 = 780
y2 = 0
speed = 0
frame_count = 0
road = []
died_image = pygame.image.load("died.png")
died_rect = died_image.get_rect()
write_name = pygame.image.load("write name.png")
bmw_image = pygame.image.load("bmw.png")
close = pygame.image.load(("close.png"))
start_image = pygame.image.load("start.png")
rect_btr = pygame.image.load("rect.png")
shop_image = pygame.image.load("shop.png")
finish = pygame.image.load("finish.png")
over = pygame.image.load("game over.png")
menu = pygame.image.load("images/menu2.png")
pikachu = pygame.image.load("picachu.png")
pikachu_rect = pikachu.get_rect()
pikachu_rect.top = (100)
pikachu_rects = pikachu.get_rect(top = 50,right = 300)
bentley = pygame.image.load("бентли.png")
bentley_rect = bentley.get_rect()
bentley_rect.top = (100)
bentley_rects = bentley.get_rect(top = 50,right = 500)
toad = pygame.image.load("жаба.png")
toad_rect = toad.get_rect()
toad_rect.top = (100)
toad_rects = toad.get_rect(top = 50,right = 700)
bestcar = pygame.image.load("жигули.png")
bestcar_rect = bestcar.get_rect()
bestcar_rect.top = (100)
bestcar_rects = bestcar.get_rect(top = 150,right = 300)
police = pygame.image.load("полиция.png")
police_rect = police.get_rect()
police_rect.top = (100)
police_rects = police.get_rect(top = 150,right = 500)
hotwheels = pygame.image.load("хот вилс.png")
hotwheels_rect = hotwheels.get_rect()
hotwheels_rect.top = (100)
hotwheels_rects = hotwheels.get_rect(top = 150,right = 700)
start_rect = start_image.get_rect()
start_rect.center = (400,160)
close_rect = close.get_rect()
close_rect.center = (200,100)
btr_rect = rect_btr.get_rect()
btr_rect.center = (400,100)
bmw_rect = bmw_image.get_rect()
bmw_rect.top = 100
bmw_rects = bmw_image.get_rect(top = 50,right = 100)
died_rect.right = 800
died_rect.top = random.choice([30,150])
ferrari = pygame.image.load("shokolad.png")
ferrari_rect = ferrari.get_rect()
ferrari_rects = ferrari.get_rect(top = 150,right = 100)
crash = pygame.mixer.Sound("crash.wav")
#pygame.mixer.music.load("song.wav")
#pygame.mixer.music.play(-1)
direction = "stop"
font_style = pygame.font.SysFont("ヒラキノ角コシックw9", 20)
label_b = font_style.render("GAME OVER", True, BLACK)
label_c = font_style.render("M E N U", True, BLUE)
for i in range(10, WIDTH, 100):
    road.append([i, 115, 35, 10])
damage = False
game_mode = "player"
shop = 0
car_name = ""
font_player = pygame.font.SysFont("Arial", 32)
input_box = pygame.Rect(100,100,140,50)
active = False
text = ""
color = "black"
player = 1
while run:
    if game_mode == "player":
        window.blit(write_name, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        conn = mysql.connector.connect(**dbconfig)
                        cursor = conn.cursor()
                        _SQL = """select id from users where name = (%s)"""
                        cursor.execute(_SQL, (text,))
                        player = cursor.fetchall()
                        if len(player) == 0:
                            _SQL = """insert users(name) values(%s) """
                            cursor.execute(_SQL, (text,))
                            conn.commit()
                            _SQL = """select id from users where name = (%s)"""
                            cursor.execute(_SQL, (text,))
                            player = cursor.fetchall()
                            cursor.close()
                            conn.close()
                        game_mode = "menu"
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if input_box.collidepoint(event.pos):
                            active = True
                            color = "blue"
                        else:
                            active = False
                            color = "black"
                pygame.draw.rect(window, color, input_box, 4)
                txt_surface = font_style.render(text, True, BLUE)
                width = max(200, txt_surface.get_width() + 20)
                input_box.w = width
                window.blit(txt_surface, (input_box.x + 10, input_box.y + 10))

            if game_mode == "menu":
                window.blit(menu, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if btr_rect.collidepoint(event.pos):
                                game_mode = "shop"
                            if close_rect.collidepoint(event.pos):
                                run = False
                speed = 0
                frame_count = 0
                window.blit(close, close_rect)
                window.blit(rect_btr, btr_rect)
            elif game_mode == "shop":
                window.blit(shop_image, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if bmw_rects.collidepoint(event.pos):
                                shop = bmw_image
                                car_name = "Bmw"
                                shop_rect = bmw_image.get_rect(left=50, top=100)
                                game_mode = "menu1"
                            elif ferrari_rects.collidepoint(event.pos):
                                shop = ferrari
                                car_name = "Ferrari"
                                shop_rect = ferrari.get_rect(left=50, top=100)
                                game_mode = "menu1"
                            elif pikachu_rects.collidepoint(event.pos):
                                shop = pikachu
                                car_name = "Pikachu"
                                shop_rect = pikachu.get_rect(left=50, top=100)
                                game_mode = "menu1"
                            elif bentley_rects.collidepoint(event.pos):
                                shop = bentley
                                car_name = "Bentley"
                                shop_rect = bentley.get_rect(left=50, top=100)
                                game_mode = "menu1"
                            elif bestcar_rects.collidepoint(event.pos):
                                shop = bestcar
                                car_name = "Best car"
                                shop_rect = bestcar.get_rect(left=50, top=100)
                                game_mode = "menu1"
                            elif toad_rects.collidepoint(event.pos):
                                shop = toad
                                car_name = "Toad"
                                shop_rect = toad.get_rect(left=50, top=100)
                                game_mode = "menu1"
                            elif police_rects.collidepoint(event.pos):
                                shop = police
                                car_name = "Police"
                                shop_rect = police.get_rect(left=50, top=100)
                                game_mode = "menu1"
                            elif hotwheels_rects.collidepoint(event.pos):
                                shop = hotwheels
                                car_name = "Hotwheels"
                                shop_rect = hotwheels.get_rect(left=50, top=100)
                                game_mode = "menu1"

                window.blit(bmw_image, bmw_rects)
                window.blit(ferrari, ferrari_rects)
                window.blit(pikachu, pikachu_rects)
                window.blit(bentley, bentley_rects)
                window.blit(toad, toad_rects)
                window.blit(bestcar, bestcar_rects)
                window.blit(police, police_rects)
                window.blit(hotwheels, hotwheels_rects)


            elif game_mode == "menu1":
                window.blit(menu, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if start_rect.collidepoint(event.pos):
                                game_mode = "game"
                window.blit(start_image, start_rect)
            elif game_mode == "game":

                window.fill(BLACK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            direction = "left"
                        if event.key == pygame.K_RIGHT:
                            direction = "right"
                        if event.key == pygame.K_UP:
                            direction = "up"
                        if event.key == pygame.K_DOWN:
                            direction = "down"
                    elif event.type == pygame.KEYUP:
                        direction = "stop"

                if direction == "left" and shop_rect.left > 0:
                    shop_rect.left -= 3
                if direction == "right" and shop_rect.right < WIDTH:
                    shop_rect.right += 3
                if direction == "up" and shop_rect.top > 0:
                    shop_rect.top -= 3
                if direction == "down" and shop_rect.bottom < 250:
                    shop_rect.bottom += 3

                window.fill(BLACK)

                # Анимация разметки
                for i in road:
                    if i[0] < 0:
                        i[0] = WIDTH
                    else:
                        i[0] -= 2
                    pygame.draw.rect(window, WHITE, i)

                # Анимация изображений "died"
                if died_rect.left > 0:
                    died_rect.left -= 15

                else:
                    died_rect.left = 800
                    died_rect.top = random.choice([30, 150])
                # cтолкновение
                if shop_rect.colliderect(died_rect):
                    damage += 1
                    died_rect.left = WIDTH
                    died_rect.top = random.choice([50, 150])
                # crash.play()
                label_ff = font_style.render(str(speed), True, WHITE)
                if damage >= 3:
                    game_mode = "died"
                    conn = mysql.connector.connect(**dbconfig)
                    cursor = conn.cursor()
                    _SQL = """insert into scores (user_id,score) values(%s,%s)"""
                    cursor.execute(_SQL, (player[0][0], speed))
                    conn.commit()
                    cursor.close()
                    conn.close()
                else:
                    window.blit(died_image, died_rect)
                    window.blit(label_ff, (700, 50))
                    frame_count += 1
                    speed = frame_count // 60
                    pygame.draw.rect(window, WHITE, (x2, y2, 30, 250))
                    window.blit(shop, shop_rect)


            elif game_mode == "died":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game_mode = "score"
                window.blit(over, (0, 0))
                label_s = font_style.render("YOUR SCORE     " + str(speed), True, BLUE)
                window.blit(label_s, (350, 225))
                damage = 0
                direction = "stop"


            elif game_mode == "score":
                window.blit(finish, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game_mode = "menu"
                conn = mysql.connector.connect(**dbconfig)
                cursor = conn.cursor()
                _SQL = """select u.name, max(s.score) from scores s left join users u on s.user_id = u.id group by u.id order by max(s.score) desc limit 5"""
                cursor.execute(_SQL, )
                records = cursor.fetchall()
                cursor.close()
                conn.close()
                y_pos = 75
                for i in records[-5:]:
                    score_label = font_style.render(str(i[0]) + " - " + str(i[1]), True, WHITE)
                    window.blit(score_label, (50, y_pos))
                    y_pos += 30





        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()