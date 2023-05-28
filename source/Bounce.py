import pygame

pygame.init()
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('SONOL')

image_bg = pygame.image.load("./images/Blue Sky.svg")
image_banana = pygame.image.load("./images/bananas.svg")
image_banana = pygame.transform.scale(image_banana, (60,60))

x_axis = 220
y_axis = 10
x_speed = 1
y_speed = 1
pygame.time.Clock().tick(60)
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    x_axis += x_speed
    y_axis += y_speed
    if x_axis < 0:
        x_speed = -x_speed
    elif y_axis < 0:
        y_speed = -y_speed
    elif x_axis + image_banana.get_size()[0] > background.get_size()[0]:
        x_speed = -x_speed
    elif y_axis + image_banana.get_size()[1] > background.get_size()[1]:
        y_speed = -y_speed

    x_axis += x_speed
    y_axis += y_speed

    background.blit(image_bg, (0,0)) # Display image
    background.blit(image_banana, (x_axis, y_axis))
    pygame.display.update()

pygame.quit()
