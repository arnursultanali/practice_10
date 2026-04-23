import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint - Practice 10")

    clock = pygame.time.Clock()

    radius = 15
    drawing_color = (0, 0, 255)  # Синий по умолчанию
    mode = 'brush'  # Режимы: 'brush', 'rectangle', 'circle', 'eraser'

    # Список всех нарисованных объектов, чтобы они не исчезали
    objects = []

    # Для рисования фигур (начальные координаты)
    start_pos = None

    while True:
        screen.fill((255, 255, 255))  # Белый фон

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # Клавиши для смены режимов и цветов
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: mode = 'rectangle'  # Нажми R для прямоугольника
                if event.key == pygame.K_c: mode = 'circle'  # Нажми C для круга
                if event.key == pygame.K_b: mode = 'brush'  # Нажми B для кисти
                if event.key == pygame.K_e: mode = 'eraser'  # Нажми E для ластика (Пункт 3)

                # Выбор цвета (Пункт 4)
                if event.key == pygame.K_1: drawing_color = (255, 0, 0)  # Красный
                if event.key == pygame.K_2: drawing_color = (0, 255, 0)  # Зеленый
                if event.key == pygame.K_3: drawing_color = (0, 0, 255)  # Синий
                if event.key == pygame.K_4: drawing_color = (0, 0, 0)  # Черный

            # Логика рисования
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                if mode == 'brush':
                    objects.append(('brush', event.pos, drawing_color, radius))
                elif mode == 'eraser':
                    objects.append(('brush', event.pos, (255, 255, 255), radius))

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # Если зажата левая кнопка
                    if mode == 'brush':
                        objects.append(('brush', event.pos, drawing_color, radius))
                    elif mode == 'eraser':
                        objects.append(('brush', event.pos, (255, 255, 255), radius))

            if event.type == pygame.MOUSEBUTTONUP:
                end_pos = event.pos
                if mode == 'rectangle' and start_pos:
                    objects.append(('rect', start_pos, end_pos, drawing_color))
                elif mode == 'circle' and start_pos:
                    objects.append(('circle', start_pos, end_pos, drawing_color))
                start_pos = None

        # Отрисовка всех сохраненных объектов
        for obj in objects:
            if obj[0] == 'brush':
                pygame.draw.circle(screen, obj[2], obj[1], obj[3])
            elif obj[0] == 'rect':
                # Вычисляем параметры прямоугольника
                x = min(obj[1][0], obj[2][0])
                y = min(obj[1][1], obj[2][1])
                w = abs(obj[1][0] - obj[2][0])
                h = abs(obj[1][1] - obj[2][1])
                pygame.draw.rect(screen, obj[3], (x, y, w, h), 2)
            elif obj[0] == 'circle':
                # Вычисляем радиус круга
                r = int(((obj[1][0] - obj[2][0]) ** 2 + (obj[1][1] - obj[2][1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, obj[3], obj[1], r, 2)

        # Инструкция на экране
        font = pygame.font.SysFont("Arial", 18)
        instructions = "R: Rect, C: Circle, B: Brush, E: Eraser | 1: Red, 2: Green, 3: Blue, 4: Black"
        text = font.render(instructions, True, (50, 50, 50))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)


main()