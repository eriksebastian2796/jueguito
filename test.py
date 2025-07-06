import random
import pygame
import sys
import json
import os
from constantes import ANCHO, ALTO

pygame.init()
pygame.mixer.init()

# Pantalla
"""ANCHO = 800
ALTO = 600"""
NOMBRE_JUEGO = "Monsters Hunter"
#ICONO_JUEGO = pygame.image.load("logovansi.png")
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(NOMBRE_JUEGO)
#pantalla.blit(ICONO_JUEGO, (0, 0))

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Fuente
fuente = pygame.font.Font(None, 48)
fuente_pequena = pygame.font.Font(None, 36)

# Personaje
personaje_img = pygame.image.load("assets/personaje/walk0.png")
personaje_rect = personaje_img.get_rect()
velocidad = 7

# Sonidos
sonido_disparo = pygame.mixer.Sound("assets/flecha.wav")
sonido_choque = pygame.mixer.Sound("assets/ruidomonstruo.wav")

# Puntuaciones
ARCHIVO_DATOS = "puntuaciones1.json"

# Enemigos
cantidad_enemigos = 5
velocidad_enemigo = 3

velocidad_flecha = 7

def cargar_puntuaciones():
    """
    Carga las puntuaciones almacenadas en el archivo JSON.

    Returns:
        list: Lista de diccionarios con las puntuaciones.
    """
    if os.path.exists(ARCHIVO_DATOS) and os.path.getsize(ARCHIVO_DATOS) > 0:
        with open(ARCHIVO_DATOS, 'r') as f:
            return json.load(f)
    return []

def guardar_puntuaciones(puntuaciones):
    """
    Guarda las puntuaciones en el archivo JSON.

    Args:
        puntuaciones (list): Lista de diccionarios con las puntuaciones.
    """
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump(puntuaciones, f)

def dibujar_texto(texto, x, y, color=NEGRO, fuente_usar=fuente):
    """
    Dibuja un texto en la pantalla.

    Args:
        texto (str): Texto a mostrar.
        x (int): Coordenada X.
        y (int): Coordenada Y.
        color (tuple): Color del texto.
        fuente_usar (pygame.font.Font): Fuente a utilizar.
    """
    imagen_texto = fuente_usar.render(texto, True, color)
    pantalla.blit(imagen_texto, (x, y))

def pedir_nombre():
    """
    Solicita al jugador que ingrese su nombre por teclado.

    Returns:
        str: Nombre ingresado.
    """
    nombre = ""
    escribiendo = True

    while escribiendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and len(nombre) > 0:
                    escribiendo = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif evento.unicode.isalnum() or evento.unicode == " ":
                    if len(nombre) < 12:
                        nombre += evento.unicode

        pantalla.fill(NEGRO)
        dibujar_texto("¡Perdiste!", ANCHO // 2 - 100, ALTO // 2 - 100, ROJO)
        dibujar_texto("Ingresa tu nombre:", ANCHO // 2 - 150, ALTO // 2 - 20, BLANCO)
        dibujar_texto(nombre + "|", ANCHO // 2 - 100, ALTO // 2 + 40, AZUL)
        pygame.display.flip()

    return nombre

def juego(pantalla):
    """
    Ejecuta la lógica principal del juego.
    Permite mover al personaje, disparar flechas y eliminar enemigos.
    Al perder, se solicita el nombre y se guarda la puntuación.
    """
    puntuacion = 0
    personaje_rect.centerx = ANCHO // 2
    personaje_rect.bottom = ALTO - 10

    enemigos = []
    for _ in range(cantidad_enemigos):
        x = random.randint(0, ANCHO - 50)
        y = random.randint(-600, -50)
        enemigo = pygame.Rect(x, y, 50, 50)
        enemigos.append(enemigo)

    flechas = []
    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo:
        
        fondo = pygame.image.load("assets/fondo_menu2.jpg")
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
        
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    flecha = pygame.Rect(personaje_rect.centerx - 5, personaje_rect.top - 10, 10, 20)
                    flechas.append(flecha)
                    sonido_disparo.play()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and personaje_rect.left > 0:
            personaje_rect.x -= velocidad
        if teclas[pygame.K_RIGHT] and personaje_rect.right < ANCHO:
            personaje_rect.x += velocidad

        for flecha in flechas[:]:
            flecha.y -= velocidad_flecha
            if flecha.y < 0:
                flechas.remove(flecha)

        for enemigo in enemigos:
            enemigo.y += velocidad_enemigo
            if enemigo.y > ALTO:
                enemigo.x = random.randint(0, ANCHO - 50)
                enemigo.y = random.randint(-200, -50)

        for flecha in flechas[:]:
            for enemigo in enemigos:
                if flecha.colliderect(enemigo):
                    flechas.remove(flecha)
                    enemigo.x = random.randint(0, ANCHO - 50)
                    enemigo.y = random.randint(-200, -50)
                    puntuacion += 10
                    break

        for enemigo in enemigos:
            if personaje_rect.colliderect(enemigo):
                sonido_choque.play()
                corriendo = False

        pantalla.blit(fondo, (0, 0))
        pantalla.blit(personaje_img, personaje_rect)
        for enemigo in enemigos:
            pygame.draw.rect(pantalla, ROJO, enemigo)
        for flecha in flechas:
            pygame.draw.rect(pantalla, VERDE, flecha)
        dibujar_texto(f"Puntos: {puntuacion}", 10, 10, AZUL, fuente_pequena)
        pygame.display.flip()
        reloj.tick(60)

    nombre = pedir_nombre()
    puntuaciones = cargar_puntuaciones()

    for i in range(len(puntuaciones)):
        for j in range(i + 1, len(puntuaciones)):
            if puntuaciones[j]["puntuacion"] > puntuaciones[i]["puntuacion"]:
                puntuaciones[i], puntuaciones[j] = puntuaciones[j], puntuaciones[i]

    puntuaciones.append({"nombre": nombre, "puntuacion": puntuacion})
    guardar_puntuaciones(puntuaciones)

def mostrar_ranking():
    """
    Muestra en pantalla el ranking de las mejores puntuaciones.
    Permite al jugador salir de esta pantalla con ESC.
    """
    puntuaciones = cargar_puntuaciones()

    for i in range(len(puntuaciones)):
        for j in range(i + 1, len(puntuaciones)):
            if puntuaciones[j]["puntuacion"] > puntuaciones[i]["puntuacion"]:
                puntuaciones[i], puntuaciones[j] = puntuaciones[j], puntuaciones[i]

    mostrando = True
    while mostrando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                mostrando = False

        pantalla.fill(BLANCO)
        dibujar_texto("Ranking", ANCHO // 2 - 80, 50, AZUL)

        for i, p in enumerate(puntuaciones[:5]):
            texto = f"{i+1}. {p['nombre']} - {p['puntuacion']} pts"
            dibujar_texto(texto, ANCHO // 2 - 100, 150 + i * 50, NEGRO, fuente_pequena)

        dibujar_texto("Presiona ESC para volver", ANCHO // 2 - 150, 500, ROJO, fuente_pequena)
        pygame.display.flip()

"""def menu():
    """
    #Muestra el menú principal del juego y permite navegar con las flechas.
"""
    opciones = ["Jugar", "Ver ranking", "Salir"]
    seleccion = 0
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                if evento.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                if evento.key == pygame.K_RETURN:
                    if seleccion == 0:
                        juego()
                    elif seleccion == 1:
                        mostrar_ranking()
                    elif seleccion == 2:
                        pygame.quit()
                        sys.exit()

        pantalla.fill(BLANCO)
        dibujar_texto("MONSTERS HUNTER", ANCHO // 2 - 180, 100, AZUL)

        for i, opcion in enumerate(opciones):
            color = ROJO if i == seleccion else NEGRO
            dibujar_texto(opcion, ANCHO // 2 - 70, 200 + i * 60, color)

        pygame.display.flip()
        reloj.tick(60)

menu()"""
