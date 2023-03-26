import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

done = False
posX = 300
posY = 300

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if posY > 25:
                posY -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if posY < 550:
                posY += 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if posX > 25:
                posX -= 20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if posX < 550:
                posX += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (posX, posY), 25)
    pygame.display.flip()

pygame.quit()