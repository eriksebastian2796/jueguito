import pygame
import json
import os
from Config.CONSTANTES import *

archivo_ranking = "ranking.json"

def cargar_ranking():
    if os.path.exists(archivo_ranking) and os.path.getsize(archivo_ranking) > 0:
        with open(archivo_ranking) as f:
            return json.load(f)
    return []

def guardar_puntaje(nombre, puntos):
    ranking = cargar_ranking()
    ranking.append({"nombre": nombre, "puntos": puntos})
    for i in range(len(ranking)):
        for j in range(i + 1, len(ranking)):
            if ranking[j]["puntos"] > ranking[i]["puntos"]:
                ranking[i], ranking[j] = ranking[j], ranking[i]
    with open(archivo_ranking, "w") as f:
        json.dump(ranking, f)

def pedir_nombre(pantalla):
    nombre = ""
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    escribiendo = True
    while escribiendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(nombre) > 0:
                    escribiendo = False
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif event.unicode.isalnum() or event.unicode == " ":
                    if len(nombre) < 12:
                        nombre += event.unicode
        pantalla.fill(NEGRO)
        t1 = font.render("¡Perdiste! Ingresa tu nombre:", True, BLANCO)
        t2 = font.render(nombre + "|", True, BLANCO)
        pantalla.blit(t1, (ANCHO // 2 - t1.get_width() // 2, 200))
        pantalla.blit(t2, (ANCHO // 2 - t2.get_width() // 2, 300))
        pygame.display.flip()
        clock.tick(60)
    return nombre

def mostrar_ranking(pantalla):
    ranking = cargar_ranking()
    for i in range(len(ranking)):
        for j in range(i + 1, len(ranking)):
            if ranking[j]["puntos"] > ranking[i]["puntos"]:
                ranking[i], ranking[j] = ranking[j], ranking[i]

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    mostrando = True
    while mostrando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                mostrando = False

        pantalla.fill(NEGRO)
        t1 = font.render("Ranking", True, ROJO)
        pantalla.blit(t1, (ANCHO // 2 - t1.get_width() // 2, 100))

        for i, entry in enumerate(ranking[:5]):
            texto = font.render(f"{i+1}. {entry['nombre']} - {entry['puntos']} pts", True, BLANCO)
            pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, 200 + i * 50))

        t2 = font.render("Presiona ESC para volver", True, ROJO)
        pantalla.blit(t2, (ANCHO // 2 - t2.get_width() // 2, 550))

        pygame.display.flip()
        clock.tick(60)