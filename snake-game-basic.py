#Snake-Game-Basic

import os  
import time  

# Dimensiones del tablero
ancho, alto = 30, 12

# Posición inicial de la serpiente
serpiente = [(10, 15)]

# Dirección inicial de la serpiente
direccion = (0, 1)  # Derecha

# Posición inicial de la comida
comida = (3, 3)

# Puntuación inicial
puntos = 0

# Función para dibujar el tablero
def dibujar():
    # Limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
    # Dibujar el tablero fila por fila
    for y in range(alto):
        for x in range(ancho):
            if (y, x) in serpiente:  # Dibujar la serpiente
                print('O', end='')
            elif (y, x) == comida:  # Dibujar la comida
                print('X', end='')
            else:  # Espacios vacíos
                print('.', end='')
        print()  
    # Mostrar la puntuación actual
    print(f"Puntos: {puntos}")

# Función para mover la serpiente
def mover():
    global comida, puntos
    # Calcula la nueva posición de la cabeza de la serpiente
    cabeza = (serpiente[0][0] + direccion[0], serpiente[0][1] + direccion[1])
    if cabeza == comida:  # Si la cabeza de la serpiente alcanza la comida
        comida = (cabeza[0] + 2, cabeza[1] + 2)  # Genera nueva posición de la comida
        puntos += 1  # Incrementa la puntuación
    else:
        serpiente.pop()  # Elimina el último segmento de la cola si no comió
    # Verificar colisión (paredes o consigo misma)
    if cabeza in serpiente or not (0 <= cabeza[0] < alto and 0 <= cabeza[1] < ancho):
        return False  # Fin del juego
    # Insertar la nueva cabeza en la lista
    serpiente.insert(0, cabeza)
    return True  # Continuar jugando

# Función para cambiar la dirección de movimiento
def cambiar_direccion(tecla):
    global direccion
    # Asignacion de teclas
    direcciones = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    if tecla in direcciones:
        direccion = direcciones[tecla]  

# Bucle principal del juego
while True:
    dibujar()  # Dibujar el tablero en cada iteración
    tecla = input("Mover (w/a/s/d): ").lower()  # Leer teclas ingresadas por el usuario
    cambiar_direccion(tecla)  # Cambiar la dirección según la tecla ingresada
    if not mover():  
        break
    time.sleep(0.2) 

# Mensaje de fin del juego
print("¡Game Over!")
