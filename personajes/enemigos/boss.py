import pygame
from utils import cargar_frames

from Config.CONSTANTES import (ALTO, 
                               ANCHO)

frames_boss_vuelo = cargar_frames(r"assets\Imagenes\boss\boss", 6)
frames_boss_ataque = cargar_frames(r"assets\Imagenes\boss\boss_ataque", 6)

frames_boss = frames_boss_ataque + frames_boss_vuelo

def inicio_boss()-> dict:
    "Función que reinicia los valores del boss"
    boss = {
        "x": 50,
        "y": -300,
        "vidas": 10,
        "frame": 0,
        "velocidad_y": 2,
        "velocidad_x": 1
    }
    return boss

def dibujar_boss(pantalla: pygame.Surface, boss :dict ,frames: list[pygame.Surface] = frames_boss):
    "Función que dibuja el Boss en pantalla"

    frame_actual = boss["frame"]
    imagen = frames[frame_actual]
        
    pantalla.blit(imagen, (boss["x"], boss["y"]))


def actualizar_frame_boss(boss: dict, disparo:bool = False):
    if disparo:
        boss["frame"] = -1 

    frame_actual = boss["frame"]     
    nuevo_frame = frame_actual + 1
    if nuevo_frame >= 12:
        nuevo_frame = 6
    boss["frame"] = nuevo_frame