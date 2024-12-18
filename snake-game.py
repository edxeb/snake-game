import pygame
import sys
import random

pygame.init()

# Configuración básica
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (150, 150, 150)

# Fuentes
font_title = pygame.font.SysFont(None, 72)
font_text = pygame.font.SysFont(None, 48)

# Variables del juego
clock = pygame.time.Clock()
snake = [(100, 100), (80, 100), (60, 100)]  # Posición inicial de la serpiente
direction = "RIGHT"
food = (400, 300)
game_active = False
score = 0

# Función para generar comida aleatoria
def generate_food():
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return (x, y)

# Función para mostrar el menú de inicio
def show_start_screen():
    blink = True
    while True:
        screen.fill(BLACK)

        # Título
        title = font_title.render("SNAKE GAME", True, GREEN)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 150))

        # Texto con parpadeo
        if blink:
            start_text = font_text.render("Presiona ESPACIO para comenzar", True, WHITE)
            screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 300))

        # Salir del juego
        exit_text = font_text.render("Presiona ESC para salir", True, GRAY)
        screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, 400))

        pygame.display.flip()

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Iniciar juego
                    return
                if event.key == pygame.K_ESCAPE:  # Salir del juego
                    pygame.quit()
                    sys.exit()

        blink = not blink  # Efecto de parpadeo
        clock.tick(2)

# Función para mostrar la pantalla de Game Over
def show_game_over_screen():
    screen.fill(BLACK)

    game_over_text = font_title.render("GAME OVER", True, RED)
    score_text = font_text.render(f"Puntuación Final: {score}", True, WHITE)
    restart_text = font_text.render("Presiona R para reiniciar", True, WHITE)
    exit_text = font_text.render("Presiona ESC para salir", True, GRAY)

    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 150))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 250))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, 350))
    screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, 400))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Función para dibujar la serpiente, comida y puntuación
def draw_elements():
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    score_text = font_text.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

# Función para mover la serpiente
def move_snake():
    global snake, food, score
    head_x, head_y = snake[0]

    if direction == "UP":
        head_y -= CELL_SIZE
    elif direction == "DOWN":
        head_y += CELL_SIZE
    elif direction == "LEFT":
        head_x -= CELL_SIZE
    elif direction == "RIGHT":
        head_x += CELL_SIZE

    new_head = (head_x, head_y)
    snake = [new_head] + snake
    if new_head == food:  # Comer comida
        food = generate_food()
        score += 10
    else:
        snake.pop()

# Función para detectar colisiones
def check_collisions():
    head_x, head_y = snake[0]
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        (head_x, head_y) in snake[1:]
    ):
        return True
    return False

# Función para manejar eventos
def handle_events():
    global direction, game_active
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if game_active:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

# Ciclo principal del juego
food = generate_food()
while True:
    show_start_screen()
    game_active = True
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    score = 0
    food = generate_food()

    while game_active:
        handle_events()
        move_snake()
        if check_collisions():
            result = show_game_over_screen()
            if result == "restart":
                break  # Volver al menú de inicio
        draw_elements()
        clock.tick(10)
