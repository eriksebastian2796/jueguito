"""
Módulo musica.py

Este módulo se encarga de la música y los efectos de sonido del juego.

Sirve para:
- Iniciar la música de la intro o del boss.
- Detener la música actual.
- Reproducir efectos de sonido como disparos, impactos o pérdida de vida.

Importante:
- Las rutas de los sonidos están en la carpeta assets/musica/
- Asegurate de que pygame.mixer esté inicializado antes de usar este módulo:
    pygame.mixer.init()
"""

import pygame
#es necesario importar esta funcion para saber si el mouse esta sobre un boton
from utils import esta_sobre

RUTA_MUSICA = "assets/musica/musica_fondo/"
RUTA_SFX = "assets/musica/fx/"

sfx_disparo = pygame.mixer.Sound(RUTA_SFX + "disparo_sfx.ogg")
sfx_impacto = pygame.mixer.Sound(RUTA_SFX + "impacto_murcielago_sfx.ogg")
sfx_vida = pygame.mixer.Sound(RUTA_SFX + "perder_vida_sfx.ogg")
sfx_hover = pygame.mixer.Sound(RUTA_SFX +"hover.wav")
sfx_click = pygame.mixer.Sound(RUTA_SFX +"seleccion.wav")

sfx_disparo.set_volume(0.5)
sfx_impacto.set_volume(0.5)
sfx_vida.set_volume(0.5)
sfx_hover.set_volume(0.6)
sfx_click.set_volume(0.6)

def reproducir_musica(nombre_archivo: str, loop: bool = True):
    
    """
    Reproduce una música de fondo a partir del nombre del archivo.

    Parámetros:
    - nombre_archivo (str): nombre del archivo de música.
    - loop (bool): si True, la música se repite en bucle. Por defecto es True.

    Se detiene la música actual antes de cargar la nueva.
    """
    
    pygame.mixer.music.stop()
    pygame.mixer.music.load(RUTA_MUSICA + nombre_archivo)
    pygame.mixer.music.play(-1 if loop else 0)
    
def iniciar_musica_intro():
    
    """
    Inicia la música de introducción del juego.
    """
    
    reproducir_musica("musica_intro.ogg")

def iniciar_batalla_murcielagos():
    
    """
    Inicia la música del juego general.
    """
    
    reproducir_musica("musica_batalla_murcielagos.ogg")
    
def iniciar_boss():
    
    """
    Inicia la música del boss.
    """
    
    reproducir_musica("musica_boss.ogg")
    
def detener_musica():
    
    """
    Detiene la música actual que esté sonando.
    """
    
    pygame.mixer.music.stop()
    
def sonido_disparo():
    """
    Reproduce el sonido de la ballesta.
    """
    sfx_disparo.play()

def sonido_impacto():
    """
    Reproduce el sonido cuando una flecha impacta en un enemigo.
    """
    sfx_impacto.play()

def sonido_vida():
    """
    Reproduce el sonido cuando el jugador pierde una vida.
    """
    sfx_vida.play()
    
def reproducir_sonido_boton(mouse_pos : tuple, boton : dict,\
    click_realizado : bool):
    
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
            sfx_hover.play()
            #sonido hover, es el sonido que hace cuando pasamos el mouse por encima
            boton["hover_activo"] = True
            
        if click_realizado:
            sfx_click.play()
    else:
        boton["hover_activo"] = False