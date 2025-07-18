import pygame

from utils import (cargar_frames,
                   detectar_colisiones,
                   detectar_colisiones_van,
                   detectar_colisiones_boss,
                   detectar_colisiones_van_fuego,
                   dibujar_icono_sonido,
                   mostrar_game_over,
                   mostrar_ganaste)

from Config.constantes import (ANCHO,
                               ALTO,
                               FPS,
                               SEGUNDO,
                               TIEMPO_NUEVO_MURCIELAGO,
                               TIEMPO_NUEVO_TIRO_BOSS,
                               TIEMPO_SUMAR_DIFICULTAD,
                               PUNTAJE_BOSS,
                               FUENTE_MENU)

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

from personajes.enemigos.boss import (inicio_boss,
                                      dibujar_boss,
                                      actualizar_frame_boss,
                                      frames_boss)

from tiros.propios import (disparar,
                           mover_tiros,
                           dibujar_tiros,
                           )

from tiros.boss import (disparar_boss,
                        mover_tiros_boss,
                        dibujar_tiros_boss,
                        actualizar_frame_tiro_boss,
                        frames_fuego)

from vidas import (dibujar_vidas_vh, 
                   dibujar_vidas_boss)

from musica import (iniciar_musica_murcielagos,
                    iniciar_musica_boss,
                    reproducir_musica,
                    sonido_impacto,
                    sonido_disparo,
                    sonido_disparo_boss,
                    sonido_vida,
                    des_mutear,
                    sonido_fuego,
                    detener_musica
                    )

from ranking import (pedir_nombre,
                     guardar_puntaje)

from intro_1 import intro_juego_parrafo

def jugar(pantalla: pygame.Surface, sonido_activado = True):

    jugando = intro_juego_parrafo(pantalla)
    van_hellsing["vidas"] = 5
    iniciar_musica_murcielagos()

    fondo = pygame.image.load(r"assets\Imagenes\Fondo\Fondo_8bit2.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    reloj = pygame.time.Clock()

    evento_tiempo = pygame.USEREVENT + 1
    evento_frame = pygame.USEREVENT + 2

    pygame.time.set_timer(evento_tiempo, SEGUNDO)
    pygame.time.set_timer(evento_frame, 60)

    tiempo_de_juego = 0
    timer_murcielago = 0
    timer_disparo_boss = -3
    
    puntaje = 0

    murcielagos = []
    tiros = []
    tiros_boss = []

    frames_murcielago = cargar_frames(r"assets\Imagenes\Murcielago\bat", 8)
    frames_van = cargar_frames(r"assets\Imagenes\personaje\walk", 5)
    
    boss_activo= False
    boss_derrotado = False

    
    flag_frames_vam = False
    flag_frames_murcielago = False
    flag_frames_boss = False
    flag_frames_fuego = False

    flag_inicio_boss = False
    flag_tiro_boss = False

    icono_sonido = pygame.Rect(430, 750, 40, 40)

    while jugando:    
        pantalla.blit(fondo, (0,0))
            
        nivel = tiempo_de_juego // TIEMPO_SUMAR_DIFICULTAD

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if icono_sonido.collidepoint(mouseX, mouseY):
                    sonido_activado = not sonido_activado
                    des_mutear(sonido_activado)

                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    tiros.append(disparar(van_hellsing["x"], van_hellsing["y"]))
                    sonido_disparo()
                    actualizar_frame(disparo=True)
                    
            if evento.type == evento_tiempo:
                tiempo_de_juego += 1
                if boss_activo:
                    timer_disparo_boss +=1
                else:
                    timer_murcielago += 1
                
            if evento.type == evento_frame:
                flag_frames_vam = True
                flag_frames_murcielago = True
                flag_frames_boss = True
                flag_frames_fuego = True
            

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

        if timer_murcielago >= TIEMPO_NUEVO_MURCIELAGO and not boss_activo:
            murcielagos.append(crear_murcielago(nivel))
            timer_murcielago = 0
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
        dibujar_vidas_vh(pantalla, van_hellsing["vidas"])
        dibujar_icono_sonido(pantalla, icono_sonido, sonido_activado)

        fuente = pygame.font.SysFont(FUENTE_MENU, 24)
        texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
        pantalla.blit(texto, (20,770))

        if puntaje >= PUNTAJE_BOSS and not boss_activo and not boss_derrotado: 
            flag_inicio_boss = True
            boss_activo = True

        if boss_activo:

            if flag_inicio_boss:
                boss = inicio_boss()
                iniciar_musica_boss()
                flag_inicio_boss = False
        
            if boss["y"] < 0:
                boss["y"] += boss ["velocidad_y"]
            else:
                boss["x"] += boss["velocidad_x"]

            if boss["x"] > 200 or boss["x"] < -90:
                boss["velocidad_x"] = -boss["velocidad_x"]

            if timer_disparo_boss > TIEMPO_NUEVO_TIRO_BOSS:
                tiros_nuevo = disparar_boss(boss["x"], boss["y"])
                tiros_boss.append(tiros_nuevo[0])
                tiros_boss.append(tiros_nuevo[1])
                tiros_boss.append(tiros_nuevo[2])
                sonido_disparo_boss()
                timer_disparo_boss = 0
                flag_tiro_boss = True

            mover_tiros_boss(tiros_boss)

            golpe_a_boss = detectar_colisiones_boss(tiros, boss, frames_boss)
            if golpe_a_boss > 0:
                puntaje += golpe_a_boss * 100
                boss["vidas"] -= golpe_a_boss
                sonido_impacto()
            
            daño_fuego = detectar_colisiones_van_fuego(tiros_boss, van_hellsing, frames_fuego, frames_van)
            if daño_fuego > 0:
                van_hellsing["vidas"] -= daño_fuego
                sonido_fuego()


            dibujar_boss(pantalla, boss)

            if flag_frames_boss:
                actualizar_frame_boss(boss, flag_tiro_boss)
                flag_frames_boss = False
                flag_tiro_boss = False

            if flag_frames_fuego:
                actualizar_frame_tiro_boss(tiros_boss)
                flag_frames_fuego = False

            dibujar_tiros_boss(pantalla, tiros_boss)
            dibujar_vidas_boss(pantalla, boss["vidas"])
            
            if boss["vidas"] <= 0:
                boss_activo = False
                boss_derrotado = True
                sonido_disparo_boss()
                iniciar_musica_murcielagos()
                puntaje += 1000
                jugando = False
        
        pygame.display.flip()
        reloj.tick(FPS)
    else:
        if van_hellsing["vidas"] <= 0:
            mostrar_game_over(pantalla)
        elif boss_derrotado:
            mostrar_ganaste(pantalla)

        detener_musica()
        reproducir_musica("musica_menu.ogg", True)
        
        nombre = pedir_nombre(pantalla)
        guardar_puntaje(nombre, puntaje)
        

