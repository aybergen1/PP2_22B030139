import pygame
from pygame import mixer
import datetime
pygame.init()
mixer.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
done = False
myClock = pygame.image.load('main-clock.png')
myClock = pygame.transform.scale(myClock, (400, 400))

minute_arrow = pygame.image.load('min.png')  # 30:257
minute_arrow = pygame.transform.scale(minute_arrow, (200,200))
second_arrow = pygame.image.load('sec.png')
second_arrow = pygame.transform.scale(second_arrow, (200,200))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # angleSECOND -= 1
    my_time = datetime.datetime.now()

    minuteINT = int(my_time.strftime("%M"))
    secondINT = int(my_time.strftime("%S"))


    angleMINUTE = minuteINT * 6 *-1
    angleSECOND = secondINT * 6 *-1

    minute = pygame.transform.rotate(minute_arrow, angleMINUTE)
    second = pygame.transform.rotate(second_arrow, angleSECOND)


    screen.fill((255, 255, 255))
    screen.blit(myClock, (50, 50))
    screen.blit(second, (250 - int(second.get_width() / 2), 250 - int(second.get_height() / 2)))
    screen.blit(minute, ((250 - int(minute.get_width() / 2), 250 - int(minute.get_height() / 2))))
    pygame.draw.circle(screen, (0, 0, 0), (250, 250), 22)
    pygame.display.flip()
    clock.tick(50)
    # time.sleep(1)
pygame.quit()
