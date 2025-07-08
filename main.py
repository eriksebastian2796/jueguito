import pygame
pygame.init()
pygame.mixer.init()
from intro_animada import intro_con_animacion
from menu import mostrar_menu
from constantes import ANCHO, ALTO

pantalla = pygame.display.set_mode((ANCHO, ALTO))

intro_con_animacion(pantalla)   # ⬅ Mostrar la animación primero
mostrar_menu(pantalla)  # ⬅ Ir al menú luego

pygame.quit()
