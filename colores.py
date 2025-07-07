BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AMARILLO =  (255, 255 ,0)
ROJO = (255 , 0,0)
COLOR_BOTON = (70, 130, 80)
COLOR_HOVER = (110, 160, 210)



def pedir_nombre(pantalla):
    nombre = ""
    font = pygame.font.Font(None, 36)
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre:
                    return nombre
                #if evento.key == pygame.K_BACKSPACE:
                #    nombre = nombre[:-1]
                if evento.unicode.isalnum() or evento.unicode == " ":
                    if len(nombre) < 12:
                        nombre += evento.unicode

        pantalla.fill(NEGRO)
        pantalla.blit(font.render("¡Perdiste! Ingresa tu nombre:", True, BLANCO), (ANCHO // 2 - 150, 200))
        pantalla.blit(font.render(nombre + "|", True, BLANCO), (ANCHO // 2 - 100, 300))
        pygame.display.flip()
        reloj.tick(60)
    return nombre
