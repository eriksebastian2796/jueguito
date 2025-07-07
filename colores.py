BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO =  (255, 255 ,0)
ROJO = (255 , 0,0)
COLOR_BOTON = (70, 130, 80)
COLOR_HOVER = (110, 160, 210)



def pedir_nombre(pantalla):
    nombre = ""
    font = pygame.font.Font(None, 36)
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre:
                    return nombre
                #if evento.key == pygame.K_BACKSPACE:
                #    nombre = nombre[:-1]
                if evento.unicode.isalnum() or evento.unicode == " ":
                    if len(nombre) < 12:
                        nombre += evento.unicode

        pantalla.fill(NEGRO)
        pantalla.blit(font.render("¡Perdiste! Ingresa tu nombre:", True, BLANCO), (ANCHO // 2 - 150, 200))
        pantalla.blit(font.render(nombre + "|", True, BLANCO), (ANCHO // 2 - 100, 300))
        pygame.display.flip()
        reloj.tick(60)
    return nombre

---------------------------------------------------------------------------------------------------------------------------------------------

import pygame
import pygame.mixer
from colores import *
from utils import esta_sobre


ANCHO = 480
ALTO = 700
FPS = 60

pygame.mixer.init()


sonido_hover = pygame.mixer.Sound("assets/musica/hover.wav")
sonido_click = pygame.mixer.Sound("assets/musica/seleccion.wav")

def intro():
    pygame.mixer.music.load("assets/musica/musica_menu.ogg")
    pygame.mixer.music.play(-1)
 
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Monster hunter")
    reloj = pygame.time.Clock()
    fuente_menu = pygame.font.Font("assets/fuentes/arcade_font.ttf", 34)
    titulo_img = pygame.image.load("assets/Titulo.png")
    titulo_img = pygame.transform.scale(titulo_img, (400, 400))

    
    
    fondo = pygame.image.load("assets/fondo_menu2 (1).jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    
    botones = [
        {"texto": "Saltar intro", "x": 200, "y": 600, "ancho": 100, "alto": 60},
    ]
  
    for boton in botones:
        boton["hover_activo"] = False
    
    en_menu = True
    while en_menu:
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(titulo_img, (40 , 10))
        
        
        mouseX, mouseY = pygame.mouse.get_pos()
        click_realizado = False
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                exit()
                                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                click_realizado = True
                
        for boton in botones:
            esta_hover = esta_sobre(mouseX, mouseY, boton)
            
            if esta_hover and not boton["hover_activo"]:
                sonido_hover.play()
                boton["hover_activo"] = True
            elif not esta_hover:
                boton["hover_activo"] = False
            
            color_texto = BLANCO
            if esta_hover:
                if click_realizado:
                    color_texto = AMARILLO        
                    sonido_click.play()
                    if esta_sobre(mouseX, mouseY, boton):
                        if boton["texto"] == "Saltar intro":
                            en_menu = False
                        
                
                else:
                    color_texto = ROJO
                    
            texto_renderizado = fuente_menu.render(boton["texto"], True, color_texto)
            
            pantalla.blit(texto_renderizado, (boton["x"], boton["y"]))
            
                            
        pygame.display.flip()
        reloj.tick(FPS)

