import pygame
pygame.init()
from menu import mostrar_menu
from Config.CONSTANTES import ANCHO, ALTO

pantalla = pygame.display.set_mode((ANCHO, ALTO))

mostrar_menu(pantalla)

pygame.quit()