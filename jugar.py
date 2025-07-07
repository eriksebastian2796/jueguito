import pygame

from utils import (cargar_frames,
                   detectar_colisiones,
                   detectar_colisiones_van)

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
                                             cambiar_frame_murcielago
                                             )

from tiros.propios import (disparar,
                           mover_tiros,
                           dibujar_tiros,
                           )

from ranking import (pedir_nombre,
                     guardar_puntaje)

def jugar(pantalla: pygame.Surface):

    fondo = pygame.image.load(r"assets\Imagenes\Fondo\Fondo.jpeg")
    fondo = pygame.transform.scale(fondo, (480, 800))

    #Seteo timer 
    reloj = pygame.time.Clock()

    evento_tiempo = pygame.USEREVENT + 1
    evento_frame = pygame.USEREVENT + 2

    pygame.time.set_timer(evento_tiempo, SEGUNDO)
    pygame.time.set_timer(evento_frame, 60)

    tiempo_de_juego = 0
    timer_murcielago = 0
    
    puntaje = 0

    murcielagos = []
    tiros = []

    frames_murcielago = cargar_frames(r"assets\Imagenes\Murcielago\bat", 8)
    frames_van = cargar_frames(r"assets\Imagenes\personaje\walk", 5)
    
    flag_frames_vam = False
    flag_frames_murcielago = False
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
                    
            if evento.type == evento_tiempo:
                tiempo_de_juego += 1
                timer_murcielago += 1
            
            if evento.type == evento_frame:
                flag_frames_vam = True
                flag_frames_murcielago = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            mover_personaje("izquierda")
            if flag_frames_vam:
                actualizar_frame()
                flag_frames_vam = False

        if keys[pygame.K_RIGHT]:
            mover_personaje("derecha")
            if flag_frames_vam:
                actualizar_frame()
                flag_frames_vam = False

        if keys[pygame.K_UP]:
            mover_personaje("arriba")

        if keys[pygame.K_DOWN]:
            mover_personaje("abajo")  

        if timer_murcielago >= TIEMPO_NUEVO_MURCIELAGO:
            murcielagos.append(crear_murcielago())
            timer_murcielago = 0

        mover_murcielagos(murcielagos, ANCHO)
        
        mover_tiros(tiros)

        puntaje += detectar_colisiones(tiros, murcielagos, frames_murcielago) *10
        
        daño = detectar_colisiones_van(murcielagos, van_hellsing, frames_murcielago, frames_van)
        van_hellsing["vidas"] -= daño

        if flag_frames_murcielago:
            flag_frames_murcielago = cambiar_frame_murcielago(murcielagos)

        dibujar_murcielagos(pantalla, murcielagos, frames_murcielago)
        dibujar_personaje(pantalla, frames_van)
        dibujar_tiros(pantalla, tiros)

        fuente = pygame.font.SysFont(None, 24)
        texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
        pantalla.blit(texto, (20,770))

        pygame.display.flip()
        reloj.tick(FPS)

    nombre = pedir_nombre(pantalla)
    guardar_puntaje(nombre, puntaje)

    pygame.quit()
