import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
W, H = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Game")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Настройки змейки
snake = [(100, 100), (90, 100), (80, 100)]  # Начальная позиция
snake_dir = (CELL_SIZE, 0)  # Начальное движение (вправо)

# Настройки еды
food = (200, 200)
def generate_food():
    while True:
        new_food = (random.randint(0, (W // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (H // CELL_SIZE) - 1) * CELL_SIZE)
        if new_food not in snake:  # Исключаем появление еды на змейке
            return new_food

# Начальная генерация еды
food = generate_food()

# Настройки игры
score = 0
level = 1
speed = 10  # Начальная скорость игры

# Шрифты
font = pygame.font.SysFont("comicsansms", 20)

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Управление змейкой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    
    # Движение змейки
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Проверка на столкновение со стенами
    if new_head[0] < 0 or new_head[0] >= W or new_head[1] < 0 or new_head[1] >= H:
        running = False
    
    # Проверка на столкновение с собой
    if new_head in snake:
        running = False
    
    snake.insert(0, new_head)
    
    # Проверка на съедение еды
    if new_head == food:
        score += 1
        if score % 3 == 0:  # Уровень повышается каждые 3 очка
            level += 1
            speed += 2  # Увеличение скорости
        food = generate_food()
    else:
        snake.pop()
    
    # Отрисовка еды
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    
    # Отображение счета и уровня
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()