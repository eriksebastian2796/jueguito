import pygame
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