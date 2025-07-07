"""
Modulo que contiene las funciones para mostrar el ranking
de los mejores puntajes de los jugadores
"""

import json
import os
import pygame
from Config.CONSTANTES import ANCHO, ALTO, BLANCO

ARCHIVO_PUNTOS = "puntuaciones1.json"
def dibujar_texto(superficie : pygame.Surface, texto : str, x : int,\
    y : int, color : tuple, fuente : pygame.font.Font):
    
    """
    Dibuja un texto en pantalla utilizando una fuente, un color especificados
    y lo muestra en la posición indicada dentro de la superficie proporcionada
    (por ejemplo, la pantalla principal del juego).

    Args:
        superficie (pygame.Surface): Superficie donde se dibujará el texto.
        texto (str): Cadena de texto a mostrar.
        x (int): Coordenada X donde se posicionará el texto.
        y (int): Coordenada Y donde se posicionará el texto.
        color (tuple): Color del texto en formato RGB.
        fuente (pygame.font.Font): Objeto de fuente usado para renderizar el texto.
    """
    
    render = fuente.render(texto, True, color)
    superficie.blit(render, (x, y))

def cargar_puntuaciones()-> list:
    
    """
    Carga las puntuaciones desde un archivo JSON. Verifica si el archivo
    de puntuaciones existe y no está vacío.
    Si se cumplen ambas condiciones, abre el archivo y carga su contenido
    como una lista de diccionarios usando `json.load()`. Si no, retorna una
    lista vacía.

    Returns:
        list: Lista de diccionarios con las puntuaciones cargadas del archivo.
              Si el archivo no existe o está vacío, retorna una lista vacía.
    """
    
    if os.path.exists(ARCHIVO_PUNTOS) and os.path.getsize(ARCHIVO_PUNTOS) > 0:
        with open(ARCHIVO_PUNTOS, "r") as archivo_json:
            # Abre el archivo en modo lectura ("r") y lo guarda como "archivo_json".
            # "with" se usa para que el archivo se cierre solo cuando termine de usarse.
            return json.load(archivo_json)
    return []

def ordernar_por_puntos(puntos : dict)-> int:
    
    """
    Devuelve la puntuación de un jugador.

    Se utiliza como clave (`key`) para ordenar una lista de diccionarios
    que representan puntuaciones. Cada diccionario debe contener una clave "puntuacion".

    Args:
        puntos (dict): Diccionario con los datos de un jugador, incluyendo la clave "puntuacion".

    Returns:
        int: Valor numérico de la puntuación del jugador.
    """
    
    return puntos["puntuacion"]

def mostrar_ranking(pantalla : pygame.Surface ,\
    fuente : pygame.font.Font, fondo : pygame.Surface):
    
    """
    Carga las puntuaciones guardadas desde un archivo JSON,
    las ordena de mayor a menor según el puntaje y las muestra en pantalla 
    Permite al usuario volver al menu presionando la tecla ESC o cerrando la ventana.

    Args:
        pantalla (pygame.Surface): Superficie donde se dibuja todo el contenido.
        fuente (pygame.font.Font): Fuente utilizada para renderizar el texto.
        fondo (pygame.Surface): Imagen de fondo que se muestra detrás del ranking.

    Comportamiento:
        - Si hay puntuaciones, se muestran las 5 mejores.
        - Si no hay puntuaciones, se muestra un mensaje de aviso.
        - Se puede salir de esta pantalla con ESC o cerrando la ventana.
    """
    
    puntuaciones = cargar_puntuaciones()
    
    puntuaciones.sort(key=ordernar_por_puntos, reverse=True)
    #Usa como clave la función "ordernar_por_puntos", que devuelve diccionario["puntuacion"]
    # reverse=True , Ordena la lista puntuaciones de mayor a menor
    
    reloj = pygame.time.Clock()
    mostrando = True
    
    while mostrando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                mostrando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                mostrando = False
                
        pantalla.blit(fondo, (0, 0))
        
        if len(puntuaciones) ==  0:
            #Pregunta si la lista de puntuaciones esta vacia
            dibujar_texto(pantalla, "No hay puntuaciones aun", ANCHO // 2 - 100, ALTO // 2 - 20, BLANCO, fuente)
        else:
            dibujar_texto(pantalla, "Ranking", ANCHO // 2 -50, 50, BLANCO, fuente)
            
            for i, puntos in enumerate(puntuaciones[:5]):
                
                """Recorre hasta las primeras 5 puntuaciones de la lista (si hay menos, recorre las que haya).
                enumerate da: [(i) la posición (0, 1, 2...)]
                puntos: el diccionario con nombre y puntuación del jugador.
                """
                
                texto = f"{i+1}. {puntos['nombre']} - {puntos['puntuacion']} pts"
                dibujar_texto(pantalla, texto, ANCHO // 2 -80, 150 + i * 50, BLANCO, fuente)
                
        dibujar_texto(pantalla, "Presiona ESC para volver", ANCHO // 2 - 130, 500, BLANCO, fuente)
        pygame.display.flip()
        
        reloj.tick(60)