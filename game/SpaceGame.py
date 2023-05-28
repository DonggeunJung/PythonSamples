import pygame
import random

def scrRect(image, x, y) :
    rect = pygame.rect.Rect(x, y, image.get_width(), image.get_height())
    return rect

pygame.init()
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('SONOL')

image_bg = pygame.image.load("./images/Moon.png")
image_bg = pygame.transform.scale(image_bg, background.get_size())
image_pico = pygame.image.load("./images/pico-a.svg")
image_pico = pygame.transform.scale(image_pico, (60, 80))
image_rocket = pygame.image.load("./images/rocketship-a.svg")
image_rocket = pygame.transform.scale(image_rocket, (60, 100))
image_star = pygame.image.load("./images/star.svg")
image_star = pygame.transform.scale(image_star, (25, 25))
image_ball = pygame.image.load("./images/ball-c.svg")
image_ball = pygame.transform.scale(image_ball, (20, 20))
font_hp = pygame.font.SysFont(None, 30)
font_gameover = pygame.font.SysFont(None, 80)

x_pos_pico = 220
to_x_pico = 0
x_pos_rocket = 210
random_rocket = random.randrange(0, background.get_size()[0] - image_rocket.get_size()[0])
stars = []
star_time = 0
random_time = random.randrange(100, 200)
balls = []
hp_rocket = 10
hp_pico = 10

pygame.time.Clock().tick(60)
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x_pico = 1
            elif event.key == pygame.K_LEFT:
                to_x_pico = -1
            elif event.key == pygame.K_SPACE:
                balls.append([x_pos_pico+15, 280])
        elif event.type == pygame.KEYUP:
            to_x_pico = 0

    x_pos_pico += to_x_pico

    if random_rocket > x_pos_rocket:
        x_pos_rocket += 0.5
    elif random_rocket < x_pos_rocket:
        x_pos_rocket -= 0.5
    else:
        random_rocket = random.randrange(0, background.get_size()[0] - image_rocket.get_size()[0])

    star_time += 1
    if star_time == random_time:
        random_time = random.randrange(100, 200)
        star_time = 0
        stars.append([x_pos_rocket+15, 100])

    background.blit(image_bg, (0, 0))  # Display image
    background.blit(image_pico, (x_pos_pico, 280))
    background.blit(image_rocket, (x_pos_rocket, 0))

    pico_rect = scrRect(image_pico, x_pos_pico, 280)
    for star in stars:
        star[1] += 1
        star_rect = scrRect(image_star, star[0], star[1])
        if pico_rect.colliderect(star_rect):
            hp_pico -= 1
            stars.remove(star)
            #print(hp_pico, hp_rocket)
            if hp_pico == 0:
                message_gameover = 'Rocket Win!'
                play = False
            continue
        if star[1] >= background.get_size()[1]:
            stars.remove(star)
        else:
            background.blit(image_star, star)

    rocket_rect = scrRect(image_rocket, x_pos_rocket, 0)
    for ball in balls:
        ball[1] -= 1
        ball_rect = scrRect(image_ball, ball[0], ball[1])
        if rocket_rect.colliderect(ball_rect):
            hp_rocket -= 1
            balls.remove(ball)
            #print(hp_pico, hp_rocket)
            if hp_rocket == 0:
                message_gameover = 'Pico Win!'
                play = False
            continue

        if ball[1] <= 0:
            balls.remove(ball)
        else:
            background.blit(image_ball, ball)

    text = font_hp.render('Pico: ' + str(hp_pico), True, (255, 255, 0))
    background.blit(text, (10, 10))
    text = font_hp.render('Rocket: ' + str(hp_rocket), True, (255, 255, 0))
    background.blit(text, (370, 10))
    pygame.display.update()

gameover_text = font_gameover.render(message_gameover, True, (255, 0, 0))
x_pos_text = (background.get_size()[0] - gameover_text.get_size()[0]) / 2
y_pos_text = (background.get_size()[1] - gameover_text.get_size()[1]) / 2
background.blit(gameover_text, (x_pos_text, y_pos_text))
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()
