import pygame

def cargar_frames(ruta_carpeta: str, cantidad_frames: int)->list[pygame.Surface]:
    frames = []
    
    for i in range(cantidad_frames):
        
        ruta = ruta_carpeta + str(i) + ".png"
        image = pygame.image.load(ruta)
        frames.append(image)
        
    return frames

def detectar_colisiones(tiros: list[dict], murcielagos: list[dict], frames_murcielagos: list[pygame.Surface]):
    for tiro in tiros:
        mask_tiro = pygame.mask.from_surface(tiro["imagen"])
        for murcielago in murcielagos:
            frame_actual = murcielago["frame"]
            mask_murcielago = pygame.mask.from_surface(frames_murcielagos[frame_actual])
            offset = (murcielago["x"] - tiro["x"] , murcielago["y"] - tiro ["y"])
            if mask_tiro.overlap(mask_murcielago, offset):
                tiros.remove(tiro)
                murcielagos.remove(murcielago)
                
def esta_sobre(mouseX, mouseY, boton):
    return (mouseX >= boton["x"] and mouseX <= boton["x"] + boton["ancho"] and \
            mouseY >= boton["y"] and mouseY <= boton["y"] + boton["alto"])