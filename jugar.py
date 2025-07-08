import pygame

from utils import (cargar_frames,
                   detectar_colisiones,
                   detectar_colisiones_van)

from Config.CONSTANTES import (ANCHO,
                               ALTO,
                               FPS,
                               SEGUNDO,
                               TIEMPO_NUEVO_MURCIELAGO,
                               TIEMPO_SUMAR_DIFICULTAD)

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

from vidas import (dibujar_vidas_vh, 
                   dibujar_vidas_boss)

from musica import (iniciar_batalla_murcielagos,
                    iniciar_boss,
                    sonido_impacto,
                    sonido_disparo,
                    sonido_vida)

from ranking import (pedir_nombre,
                     guardar_puntaje)

def jugar(pantalla: pygame.Surface):

    jugando = True
    van_hellsing["vidas"] = 5
    iniciar_batalla_murcielagos()

    fondo = pygame.image.load(r"assets\Imagenes\Fondo\Fondo_8bit2.jpg")
    fondo = pygame.transform.scale(fondo, (480, 800))

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
    
    while jugando:
        
        pantalla.blit(fondo, (0,0))
        
        nivel = tiempo_de_juego // TIEMPO_SUMAR_DIFICULTAD

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    tiros.append(disparar(van_hellsing["x"], van_hellsing["y"]))
                    sonido_disparo()
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
            murcielagos.append(crear_murcielago(nivel))

            if nivel < TIEMPO_NUEVO_MURCIELAGO - 1:
                timer_murcielago = nivel
            else:
                timer_murcielago = TIEMPO_NUEVO_MURCIELAGO - 1

        mover_murcielagos(murcielagos, ANCHO)
        
        mover_tiros(tiros)

        impacto_flecha = detectar_colisiones(tiros, murcielagos, frames_murcielago)

        if impacto_flecha > 0:
            puntaje += impacto_flecha *10
            sonido_impacto()
        
        daño = detectar_colisiones_van(murcielagos, van_hellsing, frames_murcielago, frames_van)
        if daño > 0:
            sonido_vida()
        van_hellsing["vidas"] -= daño
        if van_hellsing["vidas"] <= 0:
            jugando = False

        if flag_frames_murcielago:
            flag_frames_murcielago = cambiar_frame_murcielago(murcielagos)

        dibujar_murcielagos(pantalla, murcielagos, frames_murcielago)
        dibujar_personaje(pantalla, frames_van)
        dibujar_tiros(pantalla, tiros)
        if van_hellsing["vidas"]> 0: dibujar_vidas_vh(pantalla, van_hellsing["vidas"])

        fuente = pygame.font.SysFont(None, 24)
        texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
        pantalla.blit(texto, (20,770))

        pygame.display.flip()
        reloj.tick(FPS)
    else:
        nombre = pedir_nombre(pantalla)
        guardar_puntaje(nombre, puntaje)
