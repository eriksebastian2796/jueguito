import pygame
from personaje import (
    crear_personaje,
    cargar_frames_personaje,
    cargar_frame_arriba,
    mover_personaje,
    dibujar_personaje
)

pygame.init()
ANCHO, ALTO = 480, 700
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Sandbox Personaje")

frames_personaje = cargar_frames_personaje()
frame_arriba = cargar_frame_arriba()
personaje = crear_personaje(ANCHO, ALTO)

reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    pantalla.fill((30, 30, 40))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()
    mover_personaje(personaje, teclas, ANCHO)
    dibujar_personaje(pantalla, personaje, frames_personaje, frame_arriba, teclas)

    pygame.display.update()
    reloj.tick(60)