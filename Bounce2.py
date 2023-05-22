import pygame

def scrRect(image, scr_x, scr_y):
    scr_rect = image.get_rect()
    scr_rect.topleft = (scr_x, scr_y)
    return scr_rect

pygame.init()
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('SONOL')

image_bg = pygame.image.load("./images/Blue Sky.svg")
image_monkey = pygame.image.load("./images/monkey-a.svg") # Load image
image_monkey = pygame.transform.scale(image_monkey, (100,120)) # Resize image
image_banana = pygame.image.load("./images/bananas.svg")
image_banana = pygame.transform.scale(image_banana, (60,60))

x_pos = 180
y_pos = 240
to_x = 0

x_axis = 220
y_axis = 10
x_speed = 1
y_speed = 1
point = 0
font_text = pygame.font.SysFont(None, 30)
font_big = pygame.font.SysFont(None, 80)
gameover_text = font_big.render('GAME OVER', True, (255,0,0))
pygame.time.Clock().tick(60)
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x = 1
            elif event.key == pygame.K_LEFT:
                to_x = -1
        elif event.type == pygame.KEYUP:
            to_x = 0

    x_pos += to_x

    x_axis += x_speed
    y_axis += y_speed
    if x_axis < 0:
        x_speed = -x_speed
    elif y_axis < 0:
        y_speed = -y_speed
    elif x_axis + image_banana.get_size()[0] > background.get_size()[0]:
        x_speed = -x_speed
    elif y_axis + image_banana.get_size()[1] > background.get_size()[1]:
        #y_speed = -y_speed
        x_pos_text = (background.get_size()[0] - gameover_text.get_size()[0]) / 2
        y_pos_text = (background.get_size()[1] - gameover_text.get_size()[1]) / 2
        background.blit(gameover_text, (x_pos_text, y_pos_text))
        pygame.display.update()
        pygame.time.delay(2000)
        play = False

    rect_monkey = scrRect(image_monkey, x_pos, y_pos)
    rect_banana = scrRect(image_banana, x_axis, y_axis)
    if rect_monkey.colliderect(rect_banana):
        x_speed = -x_speed
        y_speed = -abs(y_speed)
        point += 1

    background.blit(image_bg, (0,0)) # Display image
    background.blit(image_monkey, (x_pos, y_pos))
    background.blit(image_banana, (x_axis, y_axis))
    text = font_text.render(str(point), True, (0, 0, 0))
    background.blit(text, (10, 10))
    pygame.display.update()

pygame.quit()
