import pygame
import random
from Config.CONSTANTES import (ANCHO,
                               ALTO)

def crear_murcielago(nivel: int)-> dict:

    if nivel > 8 : nivel = 8
    
    x = random.randint(0, ANCHO)
    direccion = "izquierda"
    if random.randint(0, 1) == 1:
        direccion = "derecha"
        
    murcielago = {
        "ancho": 70,
        "alto": 70,
        "x": x,
        "y": -70,
        "direccion": direccion,
        "frame": 0,
        "velocidad_x": random.randint(1, 2),
        "velocidad_y": 1 + nivel
    }
    return murcielago

def mover_murcielagos(lista_murcielagos: list [dict] , ANCHO: int)-> None:

    for murcielago in lista_murcielagos:

        murcielago["y"] = murcielago["y"] + murcielago["velocidad_y"]
        
        if murcielago["direccion"] == "derecha":
            murcielago["x"] = murcielago["x"] + murcielago["velocidad_x"]
        else:
            murcielago["x"] = murcielago["x"] - murcielago["velocidad_x"]
            
        if murcielago["x"] <=0 :
            murcielago["direccion"] = "derecha"
        elif murcielago["x"] + murcielago["ancho"] >= ANCHO:
            murcielago["direccion"] = "izquierda"

        if murcielago["y"] > ALTO:
            lista_murcielagos.remove(murcielago)

def dibujar_murcielagos(pantalla: pygame.Surface, lista_murcielagos: list [dict], frames_murcielago: list[pygame.Surface]):
    for murcielago in lista_murcielagos:
        
        frame_actual = murcielago["frame"]
        imagen_original = frames_murcielago[frame_actual]
        
        if murcielago["direccion"] == "derecha":
            imagen = pygame.transform.flip(imagen_original, True, False)
        else:
            imagen = imagen_original
        
        pantalla.blit(imagen, (murcielago["x"], murcielago["y"]))
        
def cambiar_frame_murcielago(lista_murcielagos: list[dict])-> bool:
    for murcielago in lista_murcielagos:
        frame_actual = murcielago["frame"]
        nuevo_frame = frame_actual + 1
        if nuevo_frame >= 8:
            nuevo_frame = 0
        murcielago["frame"] = nuevo_frame
    return False