# Monsters Hunter - Pygame

Monsters Hunter es un juego arcade 2D desarrollado en **Python con Pygame**, donde controlás a **Van Helsing** y debés eliminar vampiros que caen del cielo disparando flechas. ¡Cuantos más vampiros derrotes, más puntos ganás!

---

## Características del juego

- Personaje principal: **Van Helsing**, con animaciones de movimiento.
- Enemigos: **Vampiros** que caen del cielo. Al avanzar aparece un Boss
- Disparos con flechas que eliminan vampiros.
- Efectos de sonido y fondo animado con nubes.
- Sistema de puntuación con ranking guardado en un archivo `.json`.
- Interfaz de menú: Jugar, Ranking, Créditos y Salir.

---
```text
## Estructura del proyecto

MonstersHunter/
│
├── Config/                     # Configuraciones globales (constantes, tamaños, colores, etc.)
├── assets/                     # Recursos visuales y sonoros (imágenes, sonidos, sprites)
├── personajes/                 # Lógica de Van Helsing y enemigos
├── tiros/                      # Gestión de disparos y proyectiles
│
├── __init__.py                 # Inicialización del módulo principal
├── intro_animada.py           # Animación de introducción (scroll de texto)
├── intro_1.py                 # Intro animada previa a jugar
├── jugar.py                   # Lógica principal del juego en ejecución
├── main.py                    # Punto de entrada del juego
├── menu.py                    # Menú principal con opciones (Jugar, Ranking, Créditos, Salir)
├── musica.py                  # Módulo que controla la música y los efectos de sonido
├── puntuaciones1.json         # Archivo donde se guardan los puntajes de los jugadores
├── ranking.py                 # Muestra el ranking y lee/escribe los puntajes
├── utils.py                   # Funciones auxiliares compartidas
├── vidas.py                   # Lógica de control de vidas del jugador


---

## Cómo jugar

1. **Ejecutá** `main.py`.
2. Usá las **flechas del teclado** para moverte de izquierda a derecha.
3. Presioná **barra espaciadora** para disparar flechas.
4. Evitá que los vampiros te toquen.
5. Al perder, ingresá tu nombre para guardar el puntaje.

---

## Requisitos

- Python 3.10 o superior
- Pygame

### Instalación de dependencias

bash
pip install pygame



## Créditos
Código: Erik, Andi, Santi

Sprites: Creados o descargados de fuentes libres (ej. itch.io)

Sonidos: Efectos libres de uso

📄 Licencia
Este proyecto es de uso libre para fines educativos o personales. Si lo usás o modificás, ¡agradecemos que des créditos!


¡Disfrutá la caza de vampiros!

