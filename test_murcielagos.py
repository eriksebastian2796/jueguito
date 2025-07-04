import pygame
from constantes import ANCHO,ALTO
from enemigos.murcielagos import (
    crear_murcielago,
    mover_murcielagos,
    dibujar_murcielagos,
    cargar_frames_murcielagos
    )

pygame.init()
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Test murcielagos")

frame_murcielago = cargar_frames_murcielagos()
murcielagos = []
frames_spawm = 0
reloj = pygame.time.Clock()
ejecutando = True

eventos = pygame.event.get()

while ejecutando:
    pantalla.fill((150 , 150 , 150))
    
    for evento in eventos:
        if evento.type == pygame.QUIT:
            ejecutando = False
            
    frames_spawm += 1
    if frames_spawm >= 150:
        murcielagos.append(crear_murcielago())
        frames_spawm = 0
    
    mover_murcielagos(murcielagos, ANCHO)
    dibujar_murcielagos(pantalla, murcielagos, frame_murcielago)
    
    pygame.display.flip()
    reloj.tick(60)