import pygame
def cargar_frames_personaje():
    frames = []
    for i in range(8):  # si son frame0 a frame7
        ruta = "assets/personaje/walk" + str(i) + ".png"
        imagen = pygame.image.load(ruta)
        frames.append(imagen)
    return frames

def cargar_frame_arriba():
    return pygame.image.load("assets/personaje/up.png")

def crear_personaje(ancho, alto):
    personaje = {
        "x": ancho // 2,
        "y": alto - 150,  # suponiendo sprite de 64px de alto
        "direccion": "quieto",
        "frame": 0,
        "velocidad": 4,
        "animando": False
    }
    return personaje

def mover_personaje(personaje, teclas, ancho):
    if teclas[pygame.K_LEFT] and personaje["x"] > 0:
        personaje["x"] -= personaje["velocidad"]
        personaje["direccion"] = "izquierda"
        personaje["animando"] = True
    elif teclas[pygame.K_RIGHT] and personaje["x"] < ancho - 64:
        personaje["x"] += personaje["velocidad"]
        personaje["direccion"] = "derecha"
        personaje["animando"] = True
    else:
        personaje["animando"] = False
        
def dibujar_personaje(pantalla, personaje, frames, frame_arriba, teclas):
    if teclas[pygame.K_UP]:
        # Mostrar sprite apuntando hacia arriba
        imagen = frame_arriba
    else:
        # Animación si se está moviendo
        if personaje["animando"]:
            personaje["frame"] = (personaje["frame"] + 1) % len(frames)
        imagen = frames[personaje["frame"]]

        # Flip si va hacia la izquierda
        if personaje["direccion"] == "izquierda":
            imagen = pygame.transform.flip(imagen, True, False)

    # Dibujar el sprite final en pantalla
    pantalla.blit(imagen, (personaje["x"], personaje["y"]))