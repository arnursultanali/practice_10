import pygame
import time
import random

pygame.init()
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Размеры экрана и блока
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20

dis = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game - Practice 10')

clock = pygame.time.Clock()

# Шрифт
score_font = pygame.font.SysFont("comicsansms", 25)


def display_info(score, level):
    """Функция для вывода счета и уровня"""
    value = score_font.render(f"Score: {score}  Level: {level}", True, YELLOW)
    dis.blit(value, [10, 10])


def draw_snake(snake_list):
    """Отрисовка змейки"""
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])


def gameLoop():
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Начальные параметры
    score = 0
    level = 1
    snake_speed = 10

    def generate_food(snake_list):
        while True:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

            # Проверяем, не находится ли новая еда на теле змеи
            on_snake = False
            for x in snake_list:
                if x[0] == foodx and x[1] == foody:
                    on_snake = True
                    break

            if not on_snake:
                return foodx, foody

    foodx, foody = generate_food(snake_List)

    while not game_over:

        while game_close == True:
            dis.fill(BLUE)
            msg = score_font.render("You Lost! Press Q-Quit or C-Play Again", True, RED)
            dis.blit(msg, [WIDTH / 6, HEIGHT / 3])
            display_info(score, level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        # Проверка выхода за границы
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)

        # Рисуем еду
        pygame.draw.rect(dis, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка столкновения змеи с самой собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_List)
        display_info(score, level)

        pygame.display.update()

        # Если змея съела еду
        if x1 == foodx and x1 == foodx and y1 == foody:
            foodx, foody = generate_food(snake_List)
            Length_of_snake += 1
            score += 1

            # Повышение уровня каждые 3 порции еды
            if score % 3 == 0:
                level += 1
                snake_speed += 3  # Увеличиваем скорость

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()