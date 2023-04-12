# импорт библиотек
import pygame
import time
import random

snake_speed = 10

# размер окна
window_x = 720
window_y = 480

# определение цветов
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# инициализация
pygame.init()

# Инициализирование игрового окно
pygame.display.set_caption('Змейка')
game_window = pygame.display.set_mode((window_x, window_y))

# Контроллер FPS (кадры в секунду)
fps = pygame.time.Clock()

# определение положения змеи по умолчанию
snake_position = [100, 50]

# определение первых 4 блоков тела змеи
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

fruit_position2 = [random.randrange(1, (window_x // 10)) * 10,
                   random.randrange(1, (window_y // 10)) * 10]
fruit_spawn2 = True

fruit_position3 = [random.randrange(1, (window_x // 10)) * 10,
                   random.randrange(1, (window_y // 10)) * 10]
fruit_spawn3 = True

# установка направления змеи по умолчанию к
# право
direction = 'RIGHT'
change_to = direction

# начальная оценка
score = 0
level = 0


# отображение функции Score
def show_score(choice, color, font, size):
    # создание объекта шрифта score_font
    score_font = pygame.font.SysFont(font, size)

    # создать объект поверхности отображения
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # создаем прямоугольный объект для текста
    # поверхностный объект
    score_rect = score_surface.get_rect()

    # отображение текста
    game_window.blit(score_surface, score_rect)


def show_level(choice, color, font, size):
    # создание объекта шрифта score_font
    level_font = pygame.font.SysFont(font, size)

    # создать объект поверхности отображения
    # score_surface
    level_surface = level_font.render('Level : ' + str(level), True, color)

    # создаем прямоугольный объект для текста
    # поверхностный объект
    level_rect = level_surface.get_rect()

    # отображение текста
    # game_window.blit(level_surface, level_rect)

    return level_surface


# функция завершения игры
def game_over():
    # создание объекта шрифта my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # создание текстовой поверхности, на которой текст
    # будет нарисовано
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)

    # создать прямоугольный объект для текста
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # установка положения текста
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit нарисует текст на экране
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # через 2 секунды мы выйдем из программы
    time.sleep(2)

    # деактивация библиотеки pygame
    pygame.quit()

    # quit the program
    quit()


fruit3_timer = 10
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 5000)

# Main Function
while True:

    # обработка ключевых событий
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        if event.type == timer:
            fruit_spawn= False
            fruit_spawn2 =False
            fruit_spawn3  =False
    # Если две клавиши нажаты одновременно
    # мы не хотим, чтобы змея разделялась на две
    # направлений одновременно
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Перемещение змеи
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Механизм роста тела змеи
    # если фрукты и змеи сталкиваются, то очки
    # будет увеличено на 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        level += 1
        fruit_spawn = False
    if snake_position[0] == fruit_position2[0] and snake_position[1] == fruit_position2[1]:
        score += 20
        level += 1
        fruit_spawn2 = False
    if snake_position[0] == fruit_position3[0] and snake_position[1] == fruit_position3[1]:
        score += 50
        level += 1
        fruit_spawn3 = False

    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    game_window.fill(black)

    if not fruit_spawn2:
        fruit_position2 = [random.randrange(1, (window_x // 10)) * 10,
                           random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn2 = True
    game_window.fill(black)

    if not fruit_spawn3:
        fruit_position3 = [random.randrange(1, (window_x // 10)) * 10,
                           random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn3 = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    if level == 0 or level % 2 == 0 and level % 5 != 0:
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    elif level % 2 == 1 and level % 5 != 0:
        pygame.draw.rect(game_window, red, pygame.Rect(fruit_position2[0], fruit_position2[1], 10, 10))
    elif level != 0 and level % 5 == 0:
        pygame.draw.rect(game_window, "yellow", pygame.Rect(fruit_position3[0], fruit_position3[1], 10, 10))
        fruit3_timer -= 0.5
        if fruit3_timer == 0:
            level += 1
            fruit3_timer == 5

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # speed++
    if score == 30:
        snake_speed = 11
    if score == 50:
        snake_speed = 13
    if score == 70:
        snake_speed = 15
    if score == 90:
        snake_speed = 17
    if score == 100:
        snake_speed = 20

    # displaying score countinuously
    show_score(1, white, 'times new roman', 20)
    asd = show_level(2, white, 'times new roman', 20)
    game_window.blit(asd, (100, 0))
    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
