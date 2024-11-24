import pygame
import sys

pygame.init()

# Configuración básica
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake-game")

# Colores y fuente
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont(None, 48)

# Pantalla de inicio
screen.fill(BLACK)
screen.blit(font.render("SNAKE GAME", True, WHITE), (50, 100))
screen.blit(font.render("Presiona ESPACIO para comenzar", True, WHITE), (50, 200))
screen.blit(font.render("Presiona ESC para salir", True, WHITE), (50, 300)) 
pygame.display.flip()

# Esperar entrada
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Detectar cierre de ventana
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Detectar tecla ESPACIO
                screen.fill(BLACK)
                screen.blit(font.render("EL JUEGO EMPIEZA AQUÍ", True, WHITE), (50, 200))
                pygame.display.flip()
                pygame.time.wait(2000)  # Simula transición
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_ESCAPE:  # Detectar tecla ESC
                pygame.quit()
                sys.exit()
