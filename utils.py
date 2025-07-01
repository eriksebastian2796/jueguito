def esta_sobre(mouseX, mouseY, boton):
    return (mouseX >= boton["x"] and mouseX <= boton["x"] + boton["ancho"] and \
            mouseY >= boton["y"] and mouseY <= boton["y"] + boton["alto"])