import pygame
from animacion_inicio import mostrar_animacion_inicio

pygame.init()
pantalla = pygame.display.set_mode((640, 720))
mostrar_animacion_inicio(pantalla)