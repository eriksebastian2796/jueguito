import pygame

from utils import (cargar_frames,
                   detectar_colisiones)

from Config.CONSTANTES import (ANCHO,
                               ALTO,
                               FPS,
                               SEGUNDO,
                               TIEMPO_NUEVO_MURCIELAGO)

from personajes.van_hellsing import (mover_personaje,
                                     van_hellsing,
                                     dibujar_personaje,
                                     actualizar_frame,
                                     )

from personajes.enemigos.murcielagos import (crear_murcielago,
                                             mover_murcielagos,
                                             dibujar_murcielagos,
                                             )

from tiros.propios import (disparar,
                           mover_tiros,
                           dibujar_tiros,
                           )

def jugar(pantalla: pygame.Surface):

    fondo = pygame.image.load(r"assets\Imagenes\Fondo\Fondo.jpeg")
    fondo = pygame.transform.scale(fondo, (480, 800))

    #Seteo timer 
    reloj = pygame.time.Clock()

    evento_tiempo = pygame.USEREVENT + 1
    pygame.time.set_timer(evento_tiempo, SEGUNDO)

    tiempo_de_juego = 0
    timer_murcielago = 0
    
    murcielagos = []
    tiros = []

    frames_murcielago = cargar_frames(r"assets\Imagenes\Murcielago\bat", 8)
    frames_van = cargar_frames(r"assets\Imagenes\personaje\walk", 5)

    jugando = True
    while jugando:

        pantalla.blit(fondo, (0,0))
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    tiros.append(disparar(van_hellsing["x"], van_hellsing["y"]))
                    actualizar_frame(disparo=True)
                    print(tiros)
                    
            if evento.type == evento_tiempo:
                tiempo_de_juego += 1
                timer_murcielago += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mover_personaje("izquierda")
            actualizar_frame()
        if keys[pygame.K_RIGHT]:
            mover_personaje("derecha")
            actualizar_frame()
        if keys[pygame.K_UP]:
            mover_personaje("arriba")
        if keys[pygame.K_DOWN]:
            mover_personaje("abajo")  

        if timer_murcielago >= TIEMPO_NUEVO_MURCIELAGO:
            murcielagos.append(crear_murcielago())
            timer_murcielago = 0

        mover_murcielagos(murcielagos, ANCHO)
        
        mover_tiros(tiros)
        
        detectar_colisiones(tiros, murcielagos, frames_murcielago)

        dibujar_murcielagos(pantalla, murcielagos, frames_murcielago)
        dibujar_personaje(pantalla, frames_van)
        dibujar_tiros(pantalla, tiros)

        pygame.display.flip()
        reloj.tick(FPS)

    pygame.quit()

pygame.init()

#De acá para abajo se va, es solo para probarlo

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Monsters Hunter")
jugar(pantalla)
