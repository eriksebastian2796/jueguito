import random
import pygame

from constantes import ANCHO
def crear_murcielago():
    x = random.randint(0, ANCHO)
    direccion = "izquierda"
    if random.randint(0, 1) == 1:
        direccion = "derecha"
        
    murcielago = {
        "x": x,
        "y": -60,
        "direccion": direccion,
        "frame": 0,
        "velocidad_x": random.randint(1, 2),
        "velocidad_y": 0.5
    }
    return murcielago

def mover_murcielagos(lista_murcielagos, ANCHO):
    for i in range(len(lista_murcielagos)):
        murcielago = lista_murcielagos[i]
        
        murcielago["y"] = murcielago["y"] + murcielago["velocidad_y"]
        
        if murcielago["direccion"] == "derecha":
            murcielago["x"] = murcielago["x"] + murcielago["velocidad_x"]
        else:
            murcielago["x"] = murcielago["x"] - murcielago["velocidad_x"]
            
        if murcielago["x"] <=0 :
            murcielago["direccion"] = "derecha"
        elif murcielago["x"] +40 >= ANCHO:
            murcielago["direccion"] = "izquierda"
    
def dibujar_murcielagos(pantalla, lista_murcielagos, frames_base):
    cantidad_frames = len(frames_base)
    
    for i in range(len(lista_murcielagos)):
        murcielago = lista_murcielagos[i]
        
        frame_actual = murcielago["frame"]
        imagen_original = frames_base[frame_actual]
        
        if murcielago["direccion"] == "derecha":
            imagen = pygame.transform.flip(imagen_original, True, False)
        else:
            imagen = imagen_original
        
        pantalla.blit(imagen, (murcielago["x"], murcielago["y"]))
        
        nuevo_frame = frame_actual + 1
        if nuevo_frame >= cantidad_frames:
            nuevo_frame = 0
        murcielago["frame"] = nuevo_frame

def cargar_frames_murcielagos():
    frames = []
    
    for i in range(8):
        
        ruta = "assets/enemigos/murcielago/bat" + str(i) + ".png"
        image = pygame.image.load(ruta)
        frames.append(image)
        
    return frames
        
def detectar_coliciones(jugador,lista_murcielago):
    pass

def crear_murcielagos_automatico(contador , lista):
    pass

frames_murcielagos = [
    pygame.image.load("assets/enemigos/murcielago/bat0.png"),
    pygame.image.load("assets/enemigos/murcielago/bat1.png"),
    pygame.image.load("assets/enemigos/murcielago/bat2.png"),
    pygame.image.load("assets/enemigos/murcielago/bat3.png"),
    pygame.image.load("assets/enemigos/murcielago/bat4.png"),
    pygame.image.load("assets/enemigos/murcielago/bat5.png"),
    pygame.image.load("assets/enemigos/murcielago/bat6.png"),
    pygame.image.load("assets/enemigos/murcielago/bat7.png")
]