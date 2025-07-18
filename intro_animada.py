import pygame
from Config.constantes import FUENTE_MENU, AMARILLO, ANCHO, ALTO
from musica import iniciar_musica_intro, detener_musica, sfx_click

pygame.init()
pygame.mixer.init()

RUTA_FONDOS = "assets/fondos/fondo_animado/"

#Scroll = desplazamiento sobre eje X

def cargar_recursos():
    """
    Carga y devuelve todos los recursos gráficos necesarios para la animación de introducción.

    Retorna:
        imagenes (dict): Diccionario con imágenes cargadas y escaladas.
        posiciones (dict): Diccionario con posiciones (x, y) de cada fondo.
        scrolls (dict): Diccionario con posiciones iniciales de scroll para fondos con movimiento.
        velocidades (dict): Diccionario con velocidades de scroll para cada fondo.
        scrolls_niebla (dict): Diccionario con posiciones iniciales de scroll para niebla.
        velocidades_niebla (dict): Diccionario con velocidades de scroll para niebla.
    """
    imagenes = {}
    
    # Creamos un diccionario resoluciones para cada fondo

    
    resoluciones = {
        10: (ANCHO, ALTO), 9: (500, 400), 8: (200, 200), 7: (200, 100),
        6: (500, 400), 5: (400, 300), 4: (200, 100), 3: (600, 700),
        2: (220, 100), 1: (600, 400), 0: (600, 300)
    }

    # Recorre los índices del 0 al 10
    for i in range(11):
        ruta = f"{RUTA_FONDOS}fondo{i}.png"
        imagen = pygame.image.load(ruta)
        escala = resoluciones[i]
        imagen_escalada = pygame.transform.scale(imagen, escala)
        imagenes[f"fondo{i}"] = imagen_escalada
    # Carga cada imagen y la escala usando la resolución correspondiente
    

    posiciones = {
        "fondo10": (0, 0),
        "fondo9":  (-100, -100),
        "fondo8":  (100, 100),
        "fondo7":  (100, 420),
        "fondo6":  (-130, 440),
        "fondo5":  (0, 350),
        "fondo4":  (-500, 200),
        "fondo3":  (-20, ALTO - imagenes["fondo3"].get_height()), #parte inferior de la ventana restando su alto.
        "fondo2":  (0, 30),
        "fondo1":  (0, ALTO - imagenes["fondo1"].get_height()),
        "fondo0":  (-700, ALTO - imagenes["fondo0"].get_height())
    }

    # Scroll horizontal de fondos móviles
    scrolls = {}
    scrolls["fondo9"] = 0
    scrolls["fondo7"] = 0
    scrolls["fondo5"] = 0
    scrolls["fondo4"] = 0
    scrolls["fondo2"] = 0

    # Velocidades de movimiento
    velocidades = {}
    velocidades["fondo9"] = 0.2
    velocidades["fondo7"] = 0.6
    velocidades["fondo5"] = 0.7
    velocidades["fondo4"] = 0.5
    velocidades["fondo2"] = 0.4

    # Scroll horizontal de niebla
    scrolls_niebla = {}
    scrolls_niebla["fondo0"] = 0
    scrolls_niebla["fondo1"] = 0

    # Velocidades de niebla
    velocidades_niebla = {}
    velocidades_niebla["fondo0"] = 0.3
    velocidades_niebla["fondo1"] = 0.15

    return imagenes, posiciones, scrolls, velocidades, scrolls_niebla, velocidades_niebla


def dibujar_desplazamiento_fondo(nombre, scrolls, velocidades, posiciones, imagenes, pantalla, sentido="izq"):
    
    #Si sentido == "izq" se mueve a la izquierda; si no, a la derecha.
    """
    Dibuja un fondo que se desplaza horizontalmente con efecto de scroll infinito.

    Args:
        nombre (str): Nombre del fondo.
        scrolls (dict): Diccionario con posiciones actuales del scroll.
        velocidades (dict): Diccionario con velocidades de scroll para cada fondo.
        posiciones (dict): Diccionario con posiciones fijas (x, y) para cada fondo.
        imagenes (dict): Diccionario con las imágenes cargadas.
        pantalla (pygame.Surface): Superficie donde se dibuja la animación.
        sentido (str, optional): Dirección del scroll, "izq" o "der". Por defecto "izq".
    """
    if sentido == "izq":
        scrolls[nombre] -= velocidades[nombre]
        if scrolls[nombre] <= -ANCHO:
            scrolls[nombre] = 0
    #Una vez recorrido el ancho de la pantalla, se vuelve a la izquierda
            
    else:
        
    #Si el sentido no es "izq" es "der" entonces hacemos lo contrario:
        
        scrolls[nombre] += velocidades[nombre]
        if scrolls[nombre] >= ANCHO:
            scrolls[nombre] = 0

    x = scrolls[nombre]
    y = posiciones[nombre][1]
    
    #Guardamos en x la posición horizontal actual para este fondo. Y es fija.
    
    pantalla.blit(imagenes[nombre], (x, y))
    
    """Dibujamos una segunda copia del mismo fondo al lado de la primera.
        Si el fondo se mueve a la "der", dibujamos la segunda copia a la izq,es decir en x - ANCHO.
        Si el fondo se mueve a la "izq", dibujamos la segunda copia a la der, en x + ANCHO.
        De esta forma, cuando la primera imagen se mueve fuera de la pantalla, 
        la segunda aparece justo después para que no se note el borde ni que el fondo termina.
    """
    
    pantalla.blit(imagenes[nombre], (x - ANCHO if sentido == "der" else x + ANCHO, y))


def renderizar_fondos(imagenes, posiciones, scrolls, velocidades,
                      scrolls_niebla, velocidades_niebla, pantalla):
    """
    Dibuja en orden todos los fondos estáticos y con scroll, incluidos los efectos de niebla.

    Args:
        imagenes (dict): Diccionario con imágenes cargadas.
        posiciones (dict): Diccionario con posiciones (x, y) para cada fondo.
        scrolls (dict): Diccionario con posiciones actuales de scroll para fondos con scroll.
        velocidades (dict): Diccionario con velocidades para cada fondo con scroll.
        scrolls_niebla (dict): Diccionario con posiciones actuales para scroll de niebla.
        velocidades_niebla (dict): Diccionario con velocidades para scroll de niebla.
        pantalla (pygame.Surface): Superficie donde se dibuja la animación.
    """
    pantalla.blit(imagenes["fondo10"], posiciones["fondo10"])#fondo estatico
    
    #scrollea el fondo en el eje X
    dibujar_desplazamiento_fondo("fondo9", scrolls, velocidades, posiciones, imagenes, pantalla, "der")
    pantalla.blit(imagenes["fondo8"], posiciones["fondo8"])#fondo estatico
    pantalla.blit(imagenes["fondo6"], posiciones["fondo6"])#fondo estatico
    dibujar_desplazamiento_fondo("fondo7", scrolls, velocidades, posiciones, imagenes, pantalla, "izq")
    dibujar_desplazamiento_fondo("fondo4", scrolls, velocidades, posiciones, imagenes, pantalla, "izq")
    dibujar_desplazamiento_fondo("fondo5", scrolls, velocidades, posiciones, imagenes, pantalla, "der")
    pantalla.blit(imagenes["fondo3"], posiciones["fondo3"])#fondo estatico
    dibujar_desplazamiento_fondo("fondo2", scrolls, velocidades, posiciones, imagenes, pantalla, "der")

    for nombre in scrolls_niebla:
        
        #scrolls_niebla es un diccionario que guarda la posición horizontal actual de las capas de niebla
        
        scrolls_niebla[nombre] += velocidades_niebla[nombre]
        if scrolls_niebla[nombre] >= ANCHO:
            scrolls_niebla[nombre] = 0
        x = scrolls_niebla[nombre]
        y = posiciones[nombre][1]
        pantalla.blit(imagenes[nombre], (x, y))
        pantalla.blit(imagenes[nombre], (x - ANCHO, y))


def intro_con_animacion(pantalla):
    
    """
    Ejecuta la animación de introducción del juego con scrolls y efecto "Press Start".

    Reproduce la música de introducción, espera la interacción del usuario
    para continuar y detiene la música. También reproduce un sonido al hacer
    click o presionar espacio.

    Args:
        pantalla (pygame.Surface): Superficie donde se dibuja la animación.
    """
    
    iniciar_musica_intro()
    imagenes, posiciones, scrolls, velocidades, scrolls_niebla, velocidades_niebla = cargar_recursos()

    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(FUENTE_MENU, 30)
    texto_start = fuente.render("Press Start", True, AMARILLO)
    texto_rect = texto_start.get_rect(center=(ANCHO // 2, ALTO - 100))

    mostrar_texto = True
    tiempo_texto = 0
    esperando_input = True

    while esperando_input:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                detener_musica()
                sfx_click.play()
                esperando_input = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if texto_rect.collidepoint(pygame.mouse.get_pos()):
                    detener_musica()
                    sfx_click.play()
                    esperando_input = False

        renderizar_fondos(imagenes, posiciones, scrolls, velocidades,
                          scrolls_niebla, velocidades_niebla, pantalla)
        
        #Efecto "Press Start" con parpadeo
        
        tiempo_texto += reloj.get_time()
        if tiempo_texto > 500:
            mostrar_texto = not mostrar_texto
            tiempo_texto = 0
        if mostrar_texto:
            pantalla.blit(texto_start, texto_rect)

        pygame.display.flip()
        reloj.tick(60)
