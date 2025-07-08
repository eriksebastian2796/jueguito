import pygame
import pygame.mixer
from menu import mostrar_menu
from Config.CONSTANTES import ANCHO, ALTO

pygame.init()
pygame.mixer.init()

icono = pygame.image.load("assets/imagenes/vidas/vh_vida/vh_icon.png")

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Monster hunter")
pygame.display.set_icon(icono)

mostrar_menu(pantalla)

pygame.quit()