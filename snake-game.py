import pygame
import sys

# Inicialización
pygame.init()

# Configuración básica
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20  # Tamaño de cada segmento de la serpiente
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colores y fuente
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
font = pygame.font.SysFont(None, 48)

# Variables del juego
clock = pygame.time.Clock()
snake = [(100, 100), (80, 100), (60, 100)]  # Coordenadas iniciales de la serpiente
direction = "RIGHT"  # Dirección inicial
food = (400, 300)  # Posición inicial de la comida
game_active = False  # Estado del juego

# Función para dibujar la pantalla de inicio
def show_start_screen():
    screen.fill(BLACK)
    screen.blit(font.render("SNAKE GAME", True, WHITE), (50, 100))
    screen.blit(font.render("Presiona ESPACIO para comenzar", True, WHITE), (50, 200))
    screen.blit(font.render("Presiona ESC para salir", True, WHITE), (50, 300))
    pygame.display.flip()

# Función para dibujar la serpiente y la comida
def draw_elements():
    screen.fill(BLACK)  # Fondo negro
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))  # Dibujar serpiente
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))  # Dibujar comida
    pygame.display.flip()

# Lógica del movimiento
def move_snake():
    global snake
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
    snake = [new_head] + snake[:-1]  # Mover la serpiente

# Manejar eventos
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
            if not game_active and event.key == pygame.K_SPACE:
                game_active = True
            elif game_active:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

# Ciclo principal
while True:
    handle_events()
    
    if not game_active:
        show_start_screen()  # Mostrar la pantalla de inicio
    else:
        move_snake()  # Actualizar la posición de la serpiente
        draw_elements()  # Dibujar elementos del juego

    clock.tick(10)  # Controlar la velocidad del juego
