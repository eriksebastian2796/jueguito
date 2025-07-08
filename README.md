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

## Estructura del proyecto

MonstersHunter/
│
├── main.py # Archivo principal del juego
├── funciones.py # Lógica del juego y helpers
├── personajes/
│ ├── van_hellsing.py # Datos y funciones de Van Helsing
│ └── enemigos/
│ └── vampiros.py # Generación y movimiento de vampiros
├── tiros/
│ └── propios.py # Disparo de flechas
├── assets/
│ ├── Imagenes/
│ │ ├── VanHelsing/ # Sprites de Van Helsing
│ │ ├── Vampiros/ # Sprites de los enemigos
│ │ └── Fondo/ # Fondos y decoraciones
│ └── Sonidos/
│ └── disparo.wav # Efectos de sonido
├── datos/
│ └── ranking.json # Puntajes guardados
└── README.md # Este archivo


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

