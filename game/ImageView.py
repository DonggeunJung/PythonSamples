import pygame

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
x_axis = 220
y_axis = 10
to_x = 0
mousePressed = False
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
            to_y = 0
        elif event.type == pygame.MOUSEMOTION:
            if mousePressed:
                x_axis = pygame.mouse.get_pos()[0]
                y_axis = pygame.mouse.get_pos()[1]
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mousePressed = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mousePressed = False

    x_pos += to_x

    background.blit(image_bg, (0,0)) # Display image
    background.blit(image_monkey, (x_pos, y_pos))
    background.blit(image_banana, (x_axis, y_axis))

    pygame.display.update()

pygame.quit()
