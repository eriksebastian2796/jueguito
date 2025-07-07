import pygame
from Config.CONSTANTES import (ANCHO,
                               ALTO)

dimension_van = (90, 110)
sup_van_hellsing = pygame.Surface(dimension_van, pygame.SRCALPHA )

van_hellsing = { 
    "superficie" : sup_van_hellsing ,
    "dimension" : dimension_van,
    "x": (ANCHO - dimension_van[0])/2 ,
    "y": ALTO - dimension_van[1] ,
    "direccion" : "izquierda",
    "limite_y" : 600, 
    "frame" : 0,
    "vidas" : 3 ,
    "velocidad" : 4 ,
}

def mover_personaje (flecha: str, personaje: dict = van_hellsing):
        match flecha:
                case "izquierda":
                    van_hellsing["x"] -= van_hellsing["velocidad"]
                    van_hellsing["direccion"] = "izquierda"
                case "derecha":
                    van_hellsing["x"] += van_hellsing["velocidad"]
                    van_hellsing["direccion"] = "derecha"
                case "arriba":
                    van_hellsing["y"] -= van_hellsing["velocidad"]
                case "abajo":
                    van_hellsing["y"] += van_hellsing["velocidad"]

        if van_hellsing["x"]< 0:
             van_hellsing["x"] = 0             
        if van_hellsing["x"]+ van_hellsing["dimension"][0]> ANCHO:
             van_hellsing["x"] = ANCHO - van_hellsing["dimension"][0]

        if van_hellsing["y"]< van_hellsing["limite_y"]:
             van_hellsing["y"] = van_hellsing["limite_y"]
        if van_hellsing["y"]+ van_hellsing["dimension"][1] > ALTO:
             van_hellsing["y"] = ALTO - van_hellsing["dimension"][1]
             
def dibujar_personaje(pantalla: pygame.Surface, frames: list[pygame.Surface], personaje: dict = van_hellsing):
    cantidad_frames = len(frames)
    
    frame_actual = van_hellsing["frame"]
    imagen_original = frames[frame_actual]
        
    if van_hellsing["direccion"] == "izquierda":
        imagen = pygame.transform.flip(imagen_original, True, False)
    else:
        imagen = imagen_original
        
    pantalla.blit(imagen, (van_hellsing["x"], van_hellsing["y"]))

def actualizar_frame(disparo:bool = False, van_hellsing:dict = van_hellsing):
    if disparo:
        van_hellsing["frame"] = 4
    else:     
        frame_actual = van_hellsing["frame"]     
        nuevo_frame = frame_actual + 1
        if nuevo_frame >= 4:
            nuevo_frame = 0
        van_hellsing["frame"] = nuevo_frame
    
             
         
