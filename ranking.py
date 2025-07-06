import json
import os
import pygame
from constantes import ANCHO, ALTO, BLANCO, ROJO

ARCHIVO_PUNTOS = "puntuaciones1.json"
def dibujar_texto(superficie, texto, x, y, color, fuente):
    render = fuente.render(texto, True, color)
    superficie.blit(render, (x, y))

def cargar_puntuaciones():
    if os.path.exists(ARCHIVO_PUNTOS) and os.path.getsize(ARCHIVO_PUNTOS) > 0:
        with open(ARCHIVO_PUNTOS, "r") as f:
            return json.load(f)
    return []

def ordernar_por_puntos(puntos : dict):
    
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

def mostrar_ranking(pantalla , fuente):
    
    
    puntuaciones = cargar_puntuaciones()
    
    puntuaciones.sort(key=ordernar_por_puntos, reverse=True)
    
    reloj = pygame.time.Clock()
    mostrando = True
    
    while mostrando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                mostrando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                mostrando = False
                
        pantalla.fill(BLANCO)
        
        if len(puntuaciones) ==  0:
            dibujar_texto(pantalla, "No hay puntuaciones aun", ANCHO // 2 - 160, ALTO // 2 - 20, ROJO, fuente)
        else:
            dibujar_texto(pantalla, "Ranking", ANCHO // 2 - 80, 50, (0, 0, 180), fuente)
            
            for i, puntos in enumerate(puntuaciones[:5]):
                texto = f"{i+1}. {puntos['nombre']} - {puntos['puntuacion']} pts"
                dibujar_texto(pantalla, texto, ANCHO // 2 - 120, 150 + i * 50, (0, 0, 0), fuente)
                
        dibujar_texto(pantalla, "Presiona ESC para volver", ANCHO // 2 - 150, 500, ROJO, fuente)
        pygame.display.flip()
        
        reloj.tick(60)