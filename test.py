import random
import pygame
import sys
import json
import os


pygame.init()
pygame.mixer.init()

# Pantalla
ANCHO = 800
ALTO = 600
NOMBRE_JUEGO = "Monsters Hunter"
ICONO_JUEGO = pygame.image.load("logovansi.png")
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(NOMBRE_JUEGO)
pygame.display.set_icon(ICONO_JUEGO)

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Fuente
fuente = pygame.font.Font(None, 48)
fuente_pequena = pygame.font.Font(None, 36)

# Avión
avion_alto = 10
avion_ancho = 10
avion = pygame.image.load("logovansi.png")
avion_rect = avion.get_rect()
velocidad = 7

# Sonido de disparo y choque
sonido_disparo = pygame.mixer.Sound("flecha.wav")
sonido_choque = pygame.mixer.Sound("ruidomonstruo.wav")

# Puntuaciones
ARCHIVO_DATOS = "puntuaciones1.json"

# Enemigos
cantidad_enemigos = 5
velocidad_enemigo = 3

# Balas
balas = []
velocidad_bala = 7

# Funciones auxiliares
def cargar_puntuaciones():
    if os.path.exists(ARCHIVO_DATOS) and os.path.getsize(ARCHIVO_DATOS) > 0:
        with open(ARCHIVO_DATOS, 'r') as f:
            return json.load(f)
    return []

def guardar_puntuaciones(puntuaciones):
    with open(ARCHIVO_DATOS, 'w') as f:
        json.dump(puntuaciones, f)

def dibujar_texto(texto, x, y, color=NEGRO, fuente_usar=fuente):
    imagen_texto = fuente_usar.render(texto, True, color)
    pantalla.blit(imagen_texto, (x, y))

def pedir_nombre():
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

# Juego principal
def juego():
    global balas
    puntuacion = 0
    avion_rect.centerx = ANCHO // 2
    avion_rect.bottom = ALTO - 10

    enemigos = []
    for _ in range(cantidad_enemigos):
        x = random.randint(0, ANCHO - 50)
        y = random.randint(-600, -50)
        enemigo = pygame.Rect(x, y, 50, 50)
        enemigos.append(enemigo)

    balas = []
    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    bala = pygame.Rect(avion_rect.centerx - 5, avion_rect.top - 10, 10, 20)
                    balas.append(bala)
                    sonido_disparo.play()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and avion_rect.left > 0:
            avion_rect.x -= velocidad
        if teclas[pygame.K_RIGHT] and avion_rect.right < ANCHO:
            avion_rect.x += velocidad

        # Mover balas
        for bala in balas[:]:
            bala.y -= velocidad_bala
            if bala.y < 0:
                balas.remove(bala)

        # Mover enemigos
        for enemigo in enemigos:
            enemigo.y += velocidad_enemigo
            if enemigo.y > ALTO:
                enemigo.x = random.randint(0, ANCHO - 50)
                enemigo.y = random.randint(-200, -50)

        # Colisión bala-enemigo
        for bala in balas[:]:
            for enemigo in enemigos:
                if bala.colliderect(enemigo):
                    balas.remove(bala)
                    enemigo.x = random.randint(0, ANCHO - 50)
                    enemigo.y = random.randint(-200, -50)
                    puntuacion += 10
                    break

        # Colisión enemigo-avión
        for enemigo in enemigos:
            if avion_rect.colliderect(enemigo):
                sonido_choque.play()
                corriendo = False

        pantalla.fill(BLANCO)
        pantalla.blit(avion, avion_rect)
        for enemigo in enemigos:
            pygame.draw.rect(pantalla, ROJO, enemigo)
        for bala in balas:
            pygame.draw.rect(pantalla, VERDE, bala)
        dibujar_texto(f"Puntos: {puntuacion}", 10, 10, AZUL, fuente_pequena)
        pygame.display.flip()
        reloj.tick(60)

    nombre = pedir_nombre()
    puntuaciones = cargar_puntuaciones()
    puntuaciones.append({"nombre": nombre, "puntuacion": puntuacion})
    guardar_puntuaciones(puntuaciones)

def mostrar_ranking():
    puntuaciones = cargar_puntuaciones()
    puntuaciones_ordenadas = sorted(puntuaciones, key=lambda x: x["puntuacion"], reverse=True)

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

        for i, p in enumerate(puntuaciones_ordenadas[:5]):
            texto = f"{i+1}. {p['nombre']} - {p['puntuacion']} pts"
            dibujar_texto(texto, 200, 150 + i * 50, NEGRO, fuente_pequena)

        dibujar_texto("Presiona ESC para volver", 200, 500, ROJO, fuente_pequena)
        pygame.display.flip()

def menu():
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
        dibujar_texto("SHOOTER DEL AVIÓN", ANCHO // 2 - 180, 100, AZUL)

        for i, opcion in enumerate(opciones):
            color = ROJO if i == seleccion else NEGRO
            dibujar_texto(opcion, ANCHO // 2 - 70, 200 + i * 60, color)

        pygame.display.flip()
        reloj.tick(60)

# Iniciar el juego
menu()