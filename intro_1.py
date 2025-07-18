import pygame
import random
from Config.constantes import ANCHO, ALTO, FPS,BLANCO, AMARILLO, ROJO, FUENTE_MENU
from utils import (esta_sobre,)

def intro_juego_parrafo(pantalla):
    """
    Función principal de introducción animada del juego.

    Esta función se encarga de mostrar una introducción visual para el juego
    'Monsters Hunters', presentando al jugador el contexto del personaje 
    Van Helsing mediante un párrafo animado que sube por la pantalla.

    Además, renderiza un botón "Saltar Intro" que permite al jugador omitir
    esta introducción si lo desea. Se incluyen efectos visuales como lluvia
    animada y un fondo de imagen, junto a un título centrado en la parte superior.

    La función encapsula toda la lógica de la intro, incluyendo la interacción
    del mouse, la renderización de textos, animaciones, y el control de eventos.

    Returns:
        bool: 
            True si el jugador hace clic en "Saltar Intro", indicando que se debe
            continuar con el juego.
            False si el jugador cierra la ventana, útil para interrumpir el flujo.
    """


    reloj = pygame.time.Clock()
    fuente_menu = pygame.font.Font(FUENTE_MENU, 18)

    # Carga de imágenes
    titulo_img = pygame.image.load("assets/fuentes/Titulo.png")
    titulo_img = pygame.transform.scale(titulo_img, (400, 400))
    fondo = pygame.image.load("assets/fondos/fondo_intro.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

    # Definición de botón
    botones = [{"texto": "Saltar Intro", "x": 320, "y": 720, "ancho": 100, "alto": 60}]
    for boton in botones:
        boton["hover_activo"] = False

    # Texto introductorio dividido en líneas
    parrafo = [
        "La noche ha caído sobre el pueblo de Vörhelm.",
        "Sombras acechan en cada rincón,",
        "y los aldeanos viven con miedo.",
        "Los vampiros no dejan de multiplicarse,",
        "guiados por un poder antiguo y oscuro...",
        "El Rey Vampiro ha despertado.",
        "Solo uno puede detener esta pesadilla:",
        "Van Helsing, el legendario cazador.",
        "Para acabar con la maldición,",
        "deberá enfrentarse al mismísimo señor de la noche.",
        " ",
        "¿Podrás detenerlo antes ",
        "de que la oscuridad consuma el mundo?"
    ]
    
    x_parrafo = 20           # Margen izquierdo del párrafo
    y_parrafo = 550          # Posición inicial vertical
    y_limite = 400           # Altura a la que debe detenerse

    # Generación de gotas de lluvia (posiciones aleatorias)
    #Lista de coordenadas de la lluvia:
    coor_lluvia = []
    for i in range(60):
            x = random.randint(0, 480)
            y = random.randint(0, 800)
            coor_lluvia.append([x, y])

    # Bucle principal de la intro
    mostrando = True
    click_realizado = False

    while mostrando:
        eventos = pygame.event.get()
        mouseX, mouseY = pygame.mouse.get_pos()
        click_realizado = False

        # Manejo de eventos de cierre y clic
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                return False  # El jugador cerró la ventana
            if evento.type == pygame.MOUSEBUTTONDOWN:
                click_realizado = True

        # Renderizado de fondo y título
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(titulo_img, (40, 10))

        # Animación de la lluvia (movimiento vertical)
        for coor in coor_lluvia:
            x = coor[0]
            y = coor[1]
            pygame.draw.circle(pantalla, BLANCO, (x, y), 1)
            coor[1] += 1
            if coor[1] > 800:
                coor[1] = 0 

        # Renderizado del párrafo animado
        y_linea = y_parrafo
        for linea in parrafo:
            texto = fuente_menu.render(linea, True, BLANCO)
            pantalla.blit(texto, (x_parrafo, y_linea))
            y_linea += 22

        # Hacer que el párrafo suba hasta el límite definido
        if y_parrafo > y_limite:
            y_parrafo -= 0.5

        # Evaluación y render de botones
        for boton in botones:
            esta_hover = esta_sobre((mouseX, mouseY), boton)
            color_texto = BLANCO

            if esta_hover:
                if not boton["hover_activo"]:
                    boton["hover_activo"] = True
                if click_realizado:
                    color_texto = AMARILLO
                    if boton["texto"] == "Saltar Intro":
                        print("Intro saltada")
                        return True  # El jugador decidió continuar
                else:
                    color_texto = ROJO
            else:
                boton["hover_activo"] = False

            # Renderizado del texto del botón
            texto_renderizado = fuente_menu.render(boton["texto"], True, color_texto)
            pantalla.blit(texto_renderizado, (boton["x"], boton["y"]))

        # Actualizar la pantalla y mantener los FPS
        pygame.display.flip()
        reloj.tick(FPS)
