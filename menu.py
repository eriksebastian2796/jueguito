import pygame
from colores import BLANCO, AMARILLO, COLOR_BOTON, COLOR_HOVER, ROJO
from jugar import jugar
from utils import esta_sobre
from ranking import mostrar_ranking

sonido_hover = pygame.mixer.Sound("assets/musica/hover.wav")
sonido_click = pygame.mixer.Sound("assets/musica/seleccion.wav")

ANCHO = 480
ALTO = 700
FPS = 60

def mostrar_menu():
    pygame.mixer.music.load("assets/musica/musica_menu.ogg")
    pygame.mixer.music.play(-1)
 
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Monster hunter")
    reloj = pygame.time.Clock()
    fuente_menu = pygame.font.Font("assets/fuentes/arcade_font.ttf", 34)
    titulo_img = pygame.image.load("assets/Titulo.png")
    titulo_img = pygame.transform.scale(titulo_img, (400, 400))
    
    
    fondo = pygame.image.load("assets/fondo_menu.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    
    botones = [
        {"texto": "Jugar", "x": 185, "y": 400, "ancho": 200, "alto": 60},
        {"texto": "Ranking", "x": 170, "y": 450, "ancho": 200, "alto": 60},
        {"texto": "Creditos", "x": 170, "y": 500, "ancho": 200, "alto": 60},
        {"texto": "Salir", "x": 185, "y": 550, "ancho": 200, "alto": 60}
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
                en_menu = False
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
                        
                        if boton["texto"] == "Salir":
                            en_menu = False
                        elif boton["texto"] == "Ranking":
                            mostrar_ranking(pantalla)
                        # Agrega el resto de condiciones con funciones llamando a la logica que arman lo chicos
                
                else:
                    color_texto = ROJO
                    
            texto_renderizado = fuente_menu.render(boton["texto"], True, color_texto)
            pantalla.blit(texto_renderizado, (boton["x"], boton["y"]))
                            
        pygame.display.flip()
        reloj.tick(FPS)