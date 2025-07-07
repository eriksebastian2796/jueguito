import pygame

imagen = pygame.image.load(r"assets\Imagenes\Flecha\flechita.png")

dic_tiro={
    "x": 0,
    "y": 0,
    "velocidad" : 7,
    "ancho": 15,
    "alto": 30,
    "imagen": imagen 
}

def disparar(posicion_x: int, posicion_y: int)-> dict:
         
    tiro_nuevo = dic_tiro.copy()
    tiro_nuevo["x"]= posicion_x + 8
    tiro_nuevo["y"]= posicion_y
    
    return tiro_nuevo

def mover_tiros(tiros:list[dict]):
    for tiro in tiros:
        tiro["y"] -= tiro["velocidad"]
        if tiro["y"] + tiro["alto"] <= 0:
            tiros.remove(tiro)

def dibujar_tiros(pamtalla: pygame.Surface, tiros:list[dict]):
    for tiro in tiros:
        pamtalla.blit(imagen, (tiro["x"], tiro["y"]))