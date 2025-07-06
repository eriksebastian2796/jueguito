import pygame
from constantes import ANCHO, ALTO, BLANCO
def esta_sobre(mouseX, mouseY, boton):
    return (mouseX >= boton["x"] and mouseX <= boton["x"] + boton["ancho"] and \
            mouseY >= boton["y"] and mouseY <= boton["y"] + boton["alto"])
    
def cambio_color_boton(mouseX, mouseY, boton, click_realizado, color_normal, color_hover, color_click):
    esta_hover = esta_sobre(mouseX, mouseY, boton)
     
    if esta_hover:
        if click_realizado:
            return color_click
        else:
            return color_hover
    return color_normal

def reproducir_sonido_boton(mouseX, mouseY, boton, click_realizado, sonido_hover, sonido_click):
    if (mouseX >= boton["x"] and mouseX <= boton["x"] + boton["ancho"] and \
        mouseY >= boton["y"] and mouseY <= boton["y"] + boton["alto"]):
        
        if not boton.get("hover_activo", False):
            sonido_hover.play()
            boton["hover_activo"] = True
            
        if click_realizado:
            sonido_click.play()
    else:
        boton["hover_activo"] = False
        
def actualizar_sonido(eventos, mouseX, mouseY, icono_rect, sonido_activado, sonido_on_img, sonido_off_img):
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if (mouseX >= icono_rect.x and mouseX <= icono_rect.x + icono_rect.width and \
                mouseY >= icono_rect.y and mouseY <= icono_rect.y + icono_rect.height):
                
                if sonido_activado:
                    pygame.mixer.music.set_volume(0)
                    return False
                else:
                    pygame.mixer.music.set_volume(1)
                    return True
    
    return sonido_activado

def mostrar_creditos(pantalla, lista_nombres, reloj, FUENTE_MENU):
    fondo = pygame.image.load("assets/fondos/fondo_creditos.jpg")
    fuente = pygame.font.Font(FUENTE_MENU, 36)
    fuente2 = pygame.font.Font(FUENTE_MENU, 25)
    
    volver_a_menu = "Presione ESC para volver al menu"
    
    inicio_creditos_eje_y = ALTO
    
    velocidad_scroll = 0.8
    espacio_entre_lineas = 80
    
    en_creditos  = True
    while en_creditos:
        pantalla.blit(fondo, (0, 0))
        
        for i, nombre in enumerate(lista_nombres):
            render = fuente.render(nombre, True, BLANCO)
            x = (ANCHO - render.get_width()) // 2
            y = inicio_creditos_eje_y + i * espacio_entre_lineas
            pantalla.blit(render, (x, y))
       
          
        if y > 400:
            inicio_creditos_eje_y -= velocidad_scroll
        else:
            velocidad_scroll = 0
            render = fuente2.render(volver_a_menu, True, (209 , 160 , 75))
            x = (ANCHO - render.get_width()) // 2
            y = 600
            pantalla.blit(render, (x, y))
            
        
        
               
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_creditos = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                en_creditos = False
                
        pygame.display.update()
        reloj.tick(60)
           