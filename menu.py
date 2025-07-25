import pygame
from Config.constantes import ANCHO, ALTO, FPS,BLANCO, AMARILLO, ROJO, FUENTE_MENU

from utils import (esta_sobre, 
                   cambio_color_boton, 
                   actualizar_sonido, 
                   mostrar_creditos)

from ranking import mostrar_ranking
from musica import reproducir_musica, reproducir_sonido_boton
from jugar import jugar

creditos = [
    "Erik Ramirez",
    "Santiago Oggioni",
    "Andres Cespedes"
]

def mostrar_menu(pantalla):
    reproducir_musica("musica_menu.ogg", True)

    reloj = pygame.time.Clock()
    fuente_principal_grande = pygame.font.Font(FUENTE_MENU, 34)
    fuente_principal_chica = pygame.font.Font(FUENTE_MENU, 22)
    titulo_img = pygame.image.load("assets/fuentes/Titulo.png")
    titulo_img = pygame.transform.scale(titulo_img, (400, 400))
    
    sonido_on_img = pygame.image.load("assets/iconos/sonido_on.png")
    sonido_on_img = pygame.transform.scale(sonido_on_img, (40, 40))
    
    sonido_off_img = pygame.image.load("assets/iconos/sonido_off.png")
    sonido_off_img = pygame.transform.scale(sonido_off_img, (40, 40))
    
    icono_sonido = pygame.Rect(430, 750, 40, 40)
    
    
    
    fondo = pygame.image.load("assets/fondos/fondo_menu.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    fondo_ranking = pygame.image.load("assets/fondos/fondo_creditos.jpg")
    fondo_ranking = pygame.transform.scale(fondo_ranking, (ANCHO, ALTO))
    
    botones = [
        {"texto": "Jugar", "x": 185, "y": 450, "ancho": 100, "alto": 35},
        {"texto": "Ranking", "x": 170, "y": 500, "ancho": 130, "alto": 35},
        {"texto": "Creditos", "x": 170, "y": 550, "ancho": 140, "alto": 35},
        {"texto": "Salir", "x": 185, "y": 600, "ancho": 100, "alto": 35}
    ]
    
    
    for boton in botones:
        boton["hover_activo"] = False
    
    en_menu = True
    sonido_activado = True
    
    while en_menu:
        pantalla.blit(fondo, (0, 0))
        pantalla.blit(titulo_img, (40 , 10))
        
        eventos = pygame.event.get()
        mouseX, mouseY = pygame.mouse.get_pos()
        click_realizado = False
        
        for evento in eventos:
            if evento.type == pygame.QUIT:
                en_menu = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                click_realizado = True
                
        sonido_activado = actualizar_sonido(eventos, mouseX, mouseY, icono_sonido, sonido_activado)
            
        for boton in botones:
            mouse_pos = (mouseX, mouseY)
            reproducir_sonido_boton(mouse_pos, boton, click_realizado)
            color_texto = cambio_color_boton(mouse_pos, boton, click_realizado, BLANCO, ROJO, AMARILLO)
            
            if click_realizado and esta_sobre(mouse_pos, boton):
                
                
                if boton["texto"] == "Salir":
                    en_menu = False
                elif boton["texto"] == "Creditos":
                    mostrar_creditos(pantalla, creditos, reloj, FUENTE_MENU)
                elif boton["texto"] == "Ranking":
                    mostrar_ranking(pantalla, fuente_principal_chica, fondo_ranking)
                elif boton["texto"] == "Jugar":
                    jugar(pantalla, sonido_activado)
                
                
                    
                    
            texto_renderizado = fuente_principal_grande.render(boton["texto"], True, color_texto)
            pantalla.blit(texto_renderizado, (boton["x"], boton["y"]))
        
        if sonido_activado:
            pantalla.blit(sonido_on_img, (icono_sonido.x , icono_sonido.y))
        else:
            pantalla.blit(sonido_off_img, (icono_sonido.x , icono_sonido.y))
                           
        pygame.display.flip()
        reloj.tick(FPS)
        
    pygame.quit()