import pygame
import pygame.mixer
from Config.CONSTANTES import ANCHO, ALTO, FPS,BLANCO, AMARILLO, ROJO, FUENTE_MENU
from utils import esta_sobre, reproducir_sonido_boton, cambio_color_boton, actualizar_sonido, mostrar_creditos
from ranking import mostrar_ranking
from jugar import jugar

sonido_hover = pygame.mixer.Sound("assets/musica/hover.wav")
sonido_click = pygame.mixer.Sound("assets/musica/seleccion.wav")
creditos = [
    "Erik Ramirez",
    "Santiago Oggioni",
    "Andres Cespedes"
]

def mostrar_menu(pantalla):
    pygame.mixer.music.load("assets/musica/musica_menu.ogg")
    pygame.mixer.music.play(-1)
 
    pygame.display.set_caption("Monster hunter")
    reloj = pygame.time.Clock()
    fuente_principal_grande = pygame.font.Font(FUENTE_MENU, 34)
    fuente_principal_chica = pygame.font.Font(FUENTE_MENU, 22)
    titulo_img = pygame.image.load("assets/fuentes/Titulo.png")
    titulo_img = pygame.transform.scale(titulo_img, (400, 400))
    
    sonido_on_img = pygame.image.load("assets/iconos/sonido_on.png")
    sonido_on_img = pygame.transform.scale(sonido_on_img, (40, 40))
    
    sonido_off_img = pygame.image.load("assets/iconos/sonido_off.png")
    sonido_off_img = pygame.transform.scale(sonido_off_img, (40, 40))
    
    icono_sonido = sonido_on_img.get_rect()
    icono_sonido.x = int(ANCHO * 0.10)
    icono_sonido.y = int(ALTO * 0.80)
    
    
    
    fondo = pygame.image.load("assets/fondos/fondo_menu.jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    
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
            reproducir_sonido_boton(mouse_pos, boton, click_realizado, sonido_hover, sonido_click)
            color_texto = cambio_color_boton(mouse_pos, boton, click_realizado, BLANCO, ROJO, AMARILLO)
            
            if click_realizado and esta_sobre(mouse_pos, boton):
                
                
                if boton["texto"] == "Salir":
                    en_menu = False
                elif boton["texto"] == "Creditos":
                    mostrar_creditos(pantalla, creditos, reloj, FUENTE_MENU)
                elif boton["texto"] == "Ranking":
                    mostrar_ranking(pantalla, fuente_principal_chica, fondo)
                elif boton["texto"] == "Jugar":
                    jugar(pantalla)
                
                
                    
                    
            texto_renderizado = fuente_principal_grande.render(boton["texto"], True, color_texto)
            pantalla.blit(texto_renderizado, (boton["x"], boton["y"]))
        
        if sonido_activado:
            pantalla.blit(sonido_on_img, (icono_sonido.x , icono_sonido.y))
        else:
            pantalla.blit(sonido_off_img, (icono_sonido.x , icono_sonido.y))
                           
        pygame.display.flip()
        reloj.tick(FPS)
        
    pygame.quit()