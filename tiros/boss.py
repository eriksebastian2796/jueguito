import pygame

from utils import cargar_frames

from Config.constantes import (ALTO, 
                               ANCHO)


frames_fuego = cargar_frames(r"assets\Imagenes\boss\fuego_boss\0", 5)

def disparar_boss(boss_x: int, boss_y: int)-> list[dict]:
         
    tiro_nuevo1={
    "x": boss_x + 45,
    "y": boss_y + 100,
    "vel_x" : 0,
    "vel_y" : 5,
    "frame" : 0,
    }
    
    tiro_nuevo2={
    "x": boss_x + 45,
    "y": boss_y + 100,
    "vel_x" : 1,
    "vel_y" : 5,
    "frame" : 0,
    }

    tiro_nuevo3={
    "x": boss_x + 45,
    "y": boss_y + 100,
    "vel_x" : -1,
    "vel_y" : 5,
    "frame" : 0,
    }

    return [tiro_nuevo1, tiro_nuevo2, tiro_nuevo3]

def mover_tiros_boss(tiros:list[dict]):
    for tiro in tiros:
        tiro["y"] += tiro["vel_y"]
        tiro["x"] += tiro["vel_x"]

        if tiro["y"] >= ALTO:
            tiros.remove(tiro)
        if tiro["x"] >= ANCHO or tiro["x"] + 20 < 0:
            tiros.remove(tiro)


def dibujar_tiros_boss(pantalla: pygame.Surface, tiros:list[dict], frames = frames_fuego):
    for tiro in tiros:
        frame_actual = tiro["frame"]
        imagen = frames[frame_actual]
        pantalla.blit(imagen, (tiro["x"], tiro["y"]))

def actualizar_frame_tiro_boss(tiros_boss: list[dict]):
    for tiro in tiros_boss:
        frame_actual = tiro["frame"]     
        nuevo_frame = frame_actual + 1
        if nuevo_frame >= 5:
            nuevo_frame = 0
        tiro["frame"] = nuevo_frame