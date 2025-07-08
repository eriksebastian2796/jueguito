"""Modulo con funciones para marcar la cantidad de vida
    con imagenes y foto miniatura de los personajes.
"""

import pygame

RUTA_VIDAS_VH = "assets/imagenes/vidas/vh_vida/"
RUTA_ICONO_VH = RUTA_VIDAS_VH + "vh_icon.png"
RUTA_VIDAS_BOSS = "assets/imagenes/vidas/boss_vida/"
RUTA_ICONO_BOSS = RUTA_VIDAS_BOSS + "boss_icono.png"

imagenes_vidas_vh = {
    1: pygame.image.load(RUTA_VIDAS_VH + "vh1.png"),
    2: pygame.image.load(RUTA_VIDAS_VH + "vh2.png"),
    3: pygame.image.load(RUTA_VIDAS_VH + "vh3.png"),    
    4: pygame.image.load(RUTA_VIDAS_VH + "vh4.png"),
    5: pygame.image.load(RUTA_VIDAS_VH + "vh5.png")   
}

imagenes_vidas_boss = {
    0: pygame.image.load(RUTA_VIDAS_BOSS + "m0.png"),
    1: pygame.image.load(RUTA_VIDAS_BOSS + "m1.png"),
    2: pygame.image.load(RUTA_VIDAS_BOSS + "m2.png"),
    3: pygame.image.load(RUTA_VIDAS_BOSS + "m3.png"),    
    4: pygame.image.load(RUTA_VIDAS_BOSS + "m4.png"),
    5: pygame.image.load(RUTA_VIDAS_BOSS + "m5.png"),
    6: pygame.image.load(RUTA_VIDAS_BOSS + "m6.png"),
    7: pygame.image.load(RUTA_VIDAS_BOSS + "m7.png"),
    8: pygame.image.load(RUTA_VIDAS_BOSS + "m8.png"),
    9: pygame.image.load(RUTA_VIDAS_BOSS + "m9.png"),
    10: pygame.image.load(RUTA_VIDAS_BOSS + "m10.png")    
}

#Diccionario con las posiciones en el eje x e y de la barra de vidas
datos_van_helsing = {
    "x": 20,
    "y": 20,
    "separacion": -5,
    "tamano": (60, 60)
}

datos_boss = {
    "x": 400,
    "y": 600,
    "separacion": 10,
    "tamano": (60, 60)
}

icono_vh = pygame.image.load(RUTA_ICONO_VH)
icono_boss = pygame.image.load(RUTA_ICONO_BOSS)

icono_vh = pygame.transform.scale(icono_vh, datos_van_helsing["tamano"])
icono_boss = pygame.transform.scale(icono_boss, datos_van_helsing["tamano"])

def dibujar_vidas_vh(pantalla, cantidad: int):
    """
    Dibuja la barra de vidas del jugador en pantalla junto a su icono.

    Args:
        pantalla (Surface): Superficie donde se dibuja.
        cantidad (int): Cantidad de vidas (de 0 a 5).
    """
    vidas = cantidad

    pantalla.blit(icono_vh, (datos_van_helsing["x"], datos_van_helsing["y"]))
    pantalla.blit(imagenes_vidas_vh[vidas], (
    datos_van_helsing["x"] + datos_van_helsing["tamano"][0] +
    datos_van_helsing["separacion"],40)
                  
    )

def dibujar_vidas_boss(pantalla, cantidad: int):
    """
    Dibuja la barra de vidas del boss en pantalla junto a su icono.

    Args:
        pantalla (Surface): Superficie donde se dibuja.
        cantidad (int): Cantidad de vidas (de 0 a 10).
    """
    vidas = max(0, min(10, cantidad))

    pantalla.blit(icono_boss, (datos_boss["x"], datos_boss["y"]))
    pantalla.blit(imagenes_vidas_boss[vidas], ( 230 + 
    datos_boss["tamano"][0] + datos_boss["separacion"],620)
                  
    )