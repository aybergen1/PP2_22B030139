import pygame
from pygame import mixer

pygame.init()
mixer.init()
pygame.display.set_caption("player")
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
FPS = 50
done = False
n = 0
musics = ['sao1.mp3','5.mp3','klinok.mp3','sao2.mp3']
plays = ['download.png','5.png','клинок.png','5731767.png']
pause = 'стоп.png'


def start(n):
    # Loading nth audio file into our player
    mixer.music.load(musics[n])

    mixer.music.set_volume(0.2)
    # Playing our music
    mixer.music.play()


start(n)
screen.blit(pygame.image.load(plays[n]), (300, 300))
paused = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if (paused == False):
                mixer.music.pause()
                paused = True
                screen.blit(pygame.image.load(pause), (300,300))
            else:
                mixer.music.unpause()
                paused = False
                screen.blit(pygame.image.load(plays[n]), (300,300))
            # b = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if n == 4:
                n = 0
            else:
                n += 1
            screen.blit(pygame.image.load(plays[n]), (300, 300))
            start(n)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if n == 0:
                n = 4
            else:
                n -= 1
            screen.blit(pygame.image.load(plays[n]), (300, 300))
            start(n)

    pygame.display.flip()
    clock.tick(FPS)
# start(0)
pygame.quit()