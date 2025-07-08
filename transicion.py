def entre_menu_y_juego():
    pygame.mixer.music.load("assets/musica/musica_menu.ogg")
    pygame.mixer.music.play(-1)
 
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Monster hunter")
    reloj = pygame.time.Clock()
    fuente_menu = pygame.font.Font("assets/fuentes/arcade_font.ttf", 20)
    titulo_img = pygame.image.load("assets/Titulo.png")
    titulo_img = pygame.transform.scale(titulo_img, (400, 400))

    
    
    fondo = pygame.image.load("assets/fondo_menu2 (1).jpg")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    
    botones = [
        {"texto": "Continuar", "x": 350, "y": 650, "ancho": 100, "alto": 60},
    ]
  
    for boton in botones:
        boton["hover_activo"] = False
    
    en_menu = True
    while en_menu:
        pantalla.blit(fondo, (0, 0))
        #pantalla.blit(titulo_img, (40 , 10))
        
        
        mouseX, mouseY = pygame.mouse.get_pos()
        click_realizado = False
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                exit()
                                
            if evento.type == pygame.MOUSEBUTTONDOWN:
                click_realizado = True
                
        for boton in botones:
            esta_hover = esta_sobre(mouseX, mouseY, boton)
            
            if esta_hover and not boton["hover_activo"]:
                #sonido_hover.play()
                boton["hover_activo"] = True
            elif not esta_hover:
                boton["hover_activo"] = False
            
            color_texto = BLANCO
            if esta_hover:
                if click_realizado:
                    color_texto = AMARILLO        
                    #sonido_click.play()
                    if esta_sobre(mouseX, mouseY, boton):
                        if boton["texto"] == "Continuar":
                            en_menu = False
                        
                
                else:
                    color_texto = ROJO
                    
            texto_renderizado = fuente_menu.render(boton["texto"], True, color_texto)
            texto_descripcion = fuente_menu.render(f"Prepara tus flechas para matar a los enemigos...", True, BLANCO)
            texto_descripcion2 = fuente_menu.render(f"que querrán convertirte en vampiro...", True, BLANCO)
            pantalla.blit(texto_descripcion, (20, 550))
            pantalla.blit(texto_descripcion2, (20, 570))
            pantalla.blit(texto_renderizado, (boton["x"], boton["y"]))
            
                            
        pygame.display.flip()
        reloj.tick(FPS)
        reloj.tick(FPS)

