import pygame
import pygame.mixer
from Config.CONSTANTES import ANCHO, ALTO
from intro_animada import intro_con_animacion
from menu import mostrar_menu


pygame.init()
pygame.mixer.init()

icono = pygame.image.load("assets/imagenes/vidas/vh_vida/vh_icon.png")

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Monster hunter")
pygame.display.set_icon(icono)

intro_con_animacion(pantalla)
mostrar_menu(pantalla)

pygame.quit()