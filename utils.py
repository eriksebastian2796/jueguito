"""Modulos con funciones utilitarias de sonido y botones
"""

import pygame
from Config.constantes import ANCHO, ALTO, BLANCO, FUENTE_MENU

def esta_sobre(mouse_pos : tuple, boton : dict)-> bool:
    
    """
    Crea un rectángulo a partir de las coordenadas y dimensiones del botón
    y comprueba si la posición actual del mouse se encuentra dentro de ese área.

    Args:
        mouse_pos (tuple): Una tupla (x, y) con la posición actual del mouse.
        boton (dict): Diccionario que representa un botón.
            Debe contener las claves "x", "y", "ancho" y "alto".

    Returns:
        bool: True si el mouse está sobre el botón, False en caso contrario.
    """
    
    rect = pygame.Rect(boton["x"], boton["y"], boton["ancho"], boton["alto"])
    return rect.collidepoint(mouse_pos)
    
def cambio_color_boton(mouse_pos : tuple, boton :  dict,\
    click_realizado : bool, color_normal : tuple,\
    color_hover : tuple, color_click : tuple)-> tuple:
    
    esta_hover = esta_sobre(mouse_pos, boton)
    
    """
    Cambia el color del texto del botón dependiendo de si el mouse está encima
    (hover) o si se hizo clic. Si no hay interacción, se usa el color normal.

    Args:
        mouse_pos (tuple): Posición actual del mouse como una tupla (x, y).
        boton (dict): Diccionario con las claves "x", "y", "ancho" y "alto" que representa un botón.
        click_realizado (bool): True si se hizo clic con el mouse, False en caso contrario.
        [color_normal, color_hover,color_click (tuple)]

    Returns:
        tuple: El color que debe usarse actualmente para el botón.
    """
     
    if esta_hover:
        if click_realizado:
            return color_click
        else:
            return color_hover
    return color_normal

def reproducir_sonido_boton(mouse_pos : tuple, boton : dict,\
    click_realizado : bool, sonido_hover : pygame.mixer.Sound,\
    sonido_click : pygame.mixer.Sound):
    
    """
    Reproduce efectos de sonido cuando el mouse interactúa con un botón.

    Usa una clave adicional `"hover_activo"` en el diccionario del botón para 
    controlar si ya se reprodujo el sonido de hover y evitar repeticiones innecesarias.

    Args:
        mouse_pos (tuple): Posición actual del mouse como (x, y).
        boton (dict): Diccionario con las claves "x", "y", "ancho", "alto"
                      y opcionalmente "hover_activo" para seguimiento de sonido.
        click_realizado (bool): True si se hizo clic con el mouse, False si no.
        sonido_hover (pygame.mixer.Sound): Sonido a reproducir al pasar el mouse por el botón.
        sonido_click (pygame.mixer.Sound): Sonido a reproducir al hacer clic sobre el botón.

    """
    
    if esta_sobre(mouse_pos, boton):
        
        if not boton.get("hover_activo", False):
            sonido_hover.play()
            #sonido hover, es el sonido que hace cuando pasamos el mouse por encima
            boton["hover_activo"] = True
            
        if click_realizado:
            sonido_click.play()
    else:
        boton["hover_activo"] = False
        
def actualizar_sonido(eventos : list, mouseX : int, mouseY : int,\
    icono_rect : pygame.Rect, sonido_activado: bool)-> bool:
    
    """
    Alterna el estado del sonido al hacer clic sobre el ícono correspondiente.
    Utea o desmutea el juego.
    Args:
        eventos (list): Lista de eventos capturados por pygame.event.get().
        mouseX (int): Posición X actual del mouse.
        mouseY (int): Posición Y actual del mouse.
        icono_rect (pygame.Rect): Rectángulo del área del ícono de sonido.
        sonido_activado (bool): Estado actual del sonido (True si está activado).
        sonido_on_img (pygame.Surface): Imagen del ícono cuando el sonido está activado.
        sonido_off_img (pygame.Surface): Imagen del ícono cuando el sonido está desactivado.
    Returns:
        bool: Nuevo estado del sonido (True si está activado, False si está silenciado).
    """
    
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if icono_rect.collidepoint((mouseX, mouseY)):
                
                if sonido_activado:
                    pygame.mixer.music.set_volume(0)
                    return False
                else:
                    pygame.mixer.music.set_volume(1)
                    return True
    
    return sonido_activado

def mostrar_creditos(pantalla : pygame.Surface, lista_nombres : list,\
    reloj : pygame.time.Clock, FUENTE_MENU : str):
    
    """
    Muestra en pantalla los créditos del juego con efecto de scroll hacia arriba.
    Los nombres se desplazan verticalmente desde abajo hacia el centro de la pantalla.
    Una vez que los nombres llegan a cierta altura, se detiene el scroll y se muestra
    un mensaje indicando que se puede volver al menú presionando la tecla ESC.

    Args:
        pantalla (pygame.Surface): Superficie principal donde se dibujan los elementos.
        lista_nombres (list): Lista de nombres (strings) a mostrar en los créditos.
        reloj (pygame.time.Clock): Objeto Clock de Pygame para controlar los FPS.
        FUENTE_MENU (str): Ruta de la fuente utilizada para los créditos.
    """
    
    fondo = pygame.image.load("assets/fondos/fondo_creditos.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    fuente = pygame.font.Font(FUENTE_MENU, 36)
    fuente2 = pygame.font.Font(FUENTE_MENU, 25)
    
    volver_a_menu = "Presione ESC para volver al menu"
    
    inicio_creditos_eje_y = ALTO
    
    velocidad_scroll = 0.8
    espacio_entre_lineas = 80
    
    en_creditos  = True
    while en_creditos:
        fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
        pantalla.blit(fondo, (0, 0))
        
        #Recorre lista_nombres con enumerate, que da un índice [i] y un nombre
        for i, nombre in enumerate(lista_nombres):
            render = fuente.render(nombre, True, BLANCO)
            x = (ANCHO - render.get_width()) // 2
            y = inicio_creditos_eje_y + i * espacio_entre_lineas
            pantalla.blit(render, (x, y))
       
          
        if y > 400:
            #cuando los nombres todavía no llegaron al centro de la pantalla...
            #Se mueven hacia arriba restando un poquito a inicio_creditos_eje_y en cada frame.
            
            inicio_creditos_eje_y -= velocidad_scroll
        else:
            #Se detiene el scroll cuando los nombres llegan al centro de la pantalla
            velocidad_scroll = 0
            render = fuente2.render(volver_a_menu, True, (209 , 160 , 75))
            x = (ANCHO - render.get_width()) // 2
            y = 600
            pantalla.blit(render, (x, y))
            
        
        
               
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_creditos = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                en_creditos = False
                
        pygame.display.update()
        reloj.tick(60)

def cargar_frames(ruta_carpeta: str, cantidad_frames: int)->list[pygame.Surface]:
    frames = []
    
    for i in range(cantidad_frames):
        
        ruta = ruta_carpeta + str(i) + ".png"
        image = pygame.image.load(ruta)
        frames.append(image)
        
    return frames

def detectar_colisiones(tiros: list[dict], murcielagos: list[dict], frames_murcielagos: list[pygame.Surface])-> int:
    colisiones = 0
    for tiro in tiros:
        mask_tiro = pygame.mask.from_surface(tiro["imagen"])
        for murcielago in murcielagos:
            frame_actual = murcielago["frame"]
            mask_murcielago = pygame.mask.from_surface(frames_murcielagos[frame_actual])
            offset = (murcielago["x"] - tiro["x"] , murcielago["y"] - tiro ["y"])
            if mask_tiro.overlap(mask_murcielago, offset):
                tiros.remove(tiro)
                murcielagos.remove(murcielago)
                colisiones += 1
    return colisiones

def detectar_colisiones_boss(tiros: list[dict], boss: dict, frames_boss: list[pygame.Surface])-> int:
    colisiones = 0
    frame_actual_boss = boss["frame"]
    mask_boss = pygame.mask.from_surface(frames_boss[frame_actual_boss])

    for tiro in tiros:
        mask_tiro = pygame.mask.from_surface(tiro["imagen"])
        offset = (tiro["x"] - boss["x"] ,tiro["y"] - boss["y"])
        if mask_boss.overlap(mask_tiro, offset):
            colisiones += 1
            tiros.remove(tiro)
    return colisiones

def detectar_colisiones_van(murcielagos: list[dict], van_hellsing: dict, frames_murcielagos: list[pygame.Surface], frames_van: list[pygame.Surface])-> int:
    colisiones = 0
    frame_actual_van = van_hellsing["frame"]
    mask_van = pygame.mask.from_surface(frames_van[frame_actual_van])

    for murcielago in murcielagos:
        frame_actual_mur = murcielago["frame"]
        mask_murcielago = pygame.mask.from_surface(frames_murcielagos[frame_actual_mur])
        offset = (murcielago["x"] - van_hellsing["x"] ,murcielago["y"] - van_hellsing["y"])
        if mask_van.overlap(mask_murcielago, offset):
            colisiones += 1
            murcielagos.remove(murcielago)
    return colisiones

def detectar_colisiones_van_fuego(tiros_boss: list[dict], van_hellsing: dict, frames_fuego: list[pygame.Surface], frames_van: list[pygame.Surface])-> int:
    colisiones = 0
    frame_actual_van = van_hellsing["frame"]
    mask_van = pygame.mask.from_surface(frames_van[frame_actual_van])

    for tiro in tiros_boss:
        frame_actual_fuego = tiro["frame"]
        mask_fuego = pygame.mask.from_surface(frames_fuego[frame_actual_fuego])
        offset = (tiro["x"] - van_hellsing["x"] ,tiro["y"] - van_hellsing["y"])
        if mask_van.overlap(mask_fuego, offset):
            colisiones += 1
            tiros_boss.remove(tiro)
    return colisiones

def dibujar_icono_sonido(pantalla :pygame.Surface, icono_sonido: pygame.Rect, sonido_activado: bool):
    
    sonido_on_img = pygame.image.load("assets/iconos/sonido_on.png")
    sonido_on_img = pygame.transform.scale(sonido_on_img, (40, 40))
    
    sonido_off_img = pygame.image.load("assets/iconos/sonido_off.png")
    sonido_off_img = pygame.transform.scale(sonido_off_img, (40, 40))

    if sonido_activado:
        pantalla.blit(sonido_on_img, (icono_sonido.x, icono_sonido.y))
    else:
        pantalla.blit(sonido_off_img, (icono_sonido.x, icono_sonido.y))
        
def mostrar_game_over(pantalla: pygame.Surface):
    pantalla.fill((0, 0, 0)) 
    fuente = pygame.font.Font(FUENTE_MENU, 48)
    texto = fuente.render("GAME OVER", True, (255, 0, 0)) 
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2,
                          ALTO // 2 - texto.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

def mostrar_ganaste(pantalla: pygame.Surface):
    pantalla.fill((0, 0, 0)) 
    fuente = pygame.font.Font(FUENTE_MENU, 48)
    texto = fuente.render("¡GANASTE!", True, (255, 255, 255)) 
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2,
                          ALTO // 2 - texto.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)


