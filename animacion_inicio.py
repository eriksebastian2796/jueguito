import pygame
from constantes import ANCHO, ALTO, FPS, BLANCO, FUENTE_MENU
from menu import mostrar_menu

def mostrar_animacion_inicio(pantalla):
    
    frames = []
    for i in range(11):
        ruta = f"assets/fondos/fondo_animado/fondo{i}.png"
        imagen = pygame.image.load(ruta)
        imagen = pygame.transform.scale(imagen, (ANCHO, ALTO))
        frames.append(imagen)
        
    fuente = pygame.font.Font(FUENTE_MENU, 36)
    texto = fuente.render("Presione una tecla...", True, BLANCO)
    texto_rect = texto.get_rect(center=(ANCHO // 2, int(ALTO * 0.85)))
    
    reloj = pygame.time.Clock()
    ejecutando = True
    frame_actual = 0
    contador = 0
    velocidad_animacion = 5
    
    while ejecutando:
        pantalla.blit(frames[frame_actual], (0, 0))
        pantalla.blit(texto, texto_rect)
        
        pygame.display.update()
        reloj.tick(FPS)
        
        




    