import pygame
import sys
import random

# Inicialización de Pygame
pygame.init()

# Colores
blanco = (255, 255, 255)  # Definición del color blanco en RGB
negro = (0, 0, 0)          # Definición del color negro en RGB
rojo = (213, 50, 80)       # Definición del color rojo en RGB
verde = (0, 255, 0)        # Definición del color verde en RGB
azul = (50, 153, 213)      # Definición del color azul en RGB

# Dimensiones de la pantalla
ancho_pantalla = 800       # Ancho de la pantalla en píxeles
alto_pantalla = 600        # Alto de la pantalla en píxeles

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))  # Creación de la ventana de juego
pygame.display.set_caption('Snake')  # Título de la ventana

# Configuración del reloj
reloj = pygame.time.Clock()  # Reloj para controlar la velocidad del juego
velocidad_serpiente = 10     # Velocidad inicial de la serpiente

# Tamaño de los bloques de la serpiente
tamano_bloque = 40           # Tamaño en píxeles de cada bloque de la serpiente

# Cargar imágenes y redimensionarlas
imagen_cabeza = pygame.image.load('C:/Users/dicor/OneDrive/Escritorio/Juego Snake/img/cabeza_serpiente.png')  # Cargar imagen de la cabeza de la serpiente
imagen_cabeza = pygame.transform.scale(imagen_cabeza, (tamano_bloque, tamano_bloque))  # Redimensionar la imagen al tamaño de bloque
imagen_cuerpo = pygame.image.load('C:/Users/dicor/OneDrive/Escritorio/Juego Snake/img/pelota.png')  # Cargar imagen del cuerpo de la serpiente
imagen_cuerpo = pygame.transform.scale(imagen_cuerpo, (tamano_bloque, tamano_bloque))  # Redimensionar la imagen al tamaño de bloque
imagen_comida = pygame.image.load('C:/Users/dicor/OneDrive/Escritorio/Juego Snake/img/manzana.png')  # Cargar imagen de la comida (manzana)
imagen_comida = pygame.transform.scale(imagen_comida, (tamano_bloque, tamano_bloque))  # Redimensionar la imagen al tamaño de bloque

# Cargar imagen de fondo
imagen_fondo = pygame.image.load('C:/Users/dicor/OneDrive/Escritorio/Juego Snake/img/fondo.jpg')  # Cargar imagen de fondo del juego
imagen_fondo = pygame.transform.scale(imagen_fondo, (ancho_pantalla, alto_pantalla))  # Redimensionar la imagen al tamaño de la pantalla

# Cargar imagen de fondo de derrota
imagen_fondo_derrota = pygame.image.load('C:/Users/dicor/OneDrive/Escritorio/Juego Snake/img/fondoMuerte.png')  # Cargar imagen de fondo de derrota
imagen_fondo_derrota = pygame.transform.scale(imagen_fondo_derrota, (ancho_pantalla, alto_pantalla))  # Redimensionar la imagen al tamaño de la pantalla

# Fuente
fuente_estilo = pygame.font.SysFont("bahnschrift", 25)  # Definir una fuente para el mensaje de texto
fuente_puntaje = pygame.font.SysFont("comicsansms", 35)  # Definir una fuente para el puntaje

def puntaje(score):
    valor = fuente_puntaje.render("Puntaje: " + str(score), True, azul)  # Renderizar el puntaje en la pantalla
    pantalla.blit(valor, [0, 0])  # Mostrar el puntaje en la posición especificada

def nuestra_serpiente(lista_serpiente, direccion):
    for index, x in enumerate(lista_serpiente):
        if index == 0:
            cabeza_rotada = pygame.transform.rotate(imagen_cabeza, direccion)  # Rotar la cabeza de la serpiente según la dirección
            pantalla.blit(cabeza_rotada, [x[0], x[1]])  # Mostrar la cabeza de la serpiente en la posición actual
        else:
            pantalla.blit(imagen_cuerpo, [x[0], x[1]])  # Mostrar el cuerpo de la serpiente en las posiciones siguientes

def mensaje(msg, color):
    mesg = fuente_estilo.render(msg, True, color)  # Renderizar un mensaje con la fuente y color especificados
    pantalla.blit(mesg, [ancho_pantalla / 6, alto_pantalla / 3])  # Mostrar el mensaje en la posición calculada

def juego():
    game_over = False
    game_cerrado = False

    x1 = ancho_pantalla / 2  # Posición inicial X de la serpiente
    y1 = alto_pantalla / 2   # Posición inicial Y de la serpiente

    x1_cambio = 0  # Cambio en la posición X de la serpiente
    y1_cambio = 0  # Cambio en la posición Y de la serpiente

    lista_serpiente = []  # Lista para almacenar las posiciones de la serpiente
    longitud_serpiente = 1  # Longitud inicial de la serpiente

    comida_x = round(random.randrange(0, ancho_pantalla - tamano_bloque) / tamano_bloque) * tamano_bloque  # Posición X inicial aleatoria de la comida
    comida_y = round(random.randrange(0, alto_pantalla - tamano_bloque) / tamano_bloque) * tamano_bloque  # Posición Y inicial aleatoria de la comida

    direccion = 0  # Dirección inicial de la serpiente (0: hacia arriba)

    while not game_over:

        while game_cerrado:
            pantalla.blit(imagen_fondo_derrota, [0, 0])  # Mostrar la imagen de fondo de derrota
            mensaje("Perdiste! Presiona Q-Salir o C-Jugar de nuevo", rojo)  # Mostrar mensaje de derrota
            puntaje(longitud_serpiente - 1)  # Mostrar puntaje actual
            pygame.display.update()  # Actualizar la pantalla

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_cerrado = False
                    if event.key == pygame.K_c:
                        juego()  # Reiniciar el juego si se presiona la tecla C

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True  # Salir del juego si se cierra la ventana
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  # Mover a la izquierda
                    x1_cambio = -tamano_bloque
                    y1_cambio = 0
                    direccion = 90
                elif event.key == pygame.K_d:  # Mover a la derecha
                    x1_cambio = tamano_bloque
                    y1_cambio = 0
                    direccion = -90
                elif event.key == pygame.K_w:  # Mover hacia arriba
                    y1_cambio = -tamano_bloque
                    x1_cambio = 0
                    direccion = 0
                elif event.key == pygame.K_s:  # Mover hacia abajo
                    y1_cambio = tamano_bloque
                    x1_cambio = 0
                    direccion = 180

        if x1 >= ancho_pantalla or x1 < 0 or y1 >= alto_pantalla or y1 < 0:
            game_cerrado = True  # Terminar el juego si la serpiente sale de los límites de la pantalla
        x1 += x1_cambio  # Actualizar la posición X de la serpiente
        y1 += y1_cambio  # Actualizar la posición Y de la serpiente
        pantalla.blit(imagen_fondo, [0, 0])  # Mostrar la imagen de fondo del juego
        pantalla.blit(imagen_comida, [comida_x, comida_y])  # Mostrar la comida en la pantalla
        cabeza_serpiente = [x1, y1]  # Coordenadas de la cabeza de la serpiente
        lista_serpiente.insert(0, cabeza_serpiente)  # Agregar la cabeza al principio de la lista de la serpiente
        if len(lista_serpiente) > longitud_serpiente:
            lista_serpiente.pop()  # Eliminar el último elemento de la lista si la serpiente ha crecido

        for x in lista_serpiente[1:]:
            if x == cabeza_serpiente:
                game_cerrado = True  # Terminar el juego si la serpiente se choca consigo misma

        nuestra_serpiente(lista_serpiente, direccion)  # Dibujar la serpiente en la pantalla
        puntaje(longitud_serpiente - 1)  # Mostrar el puntaje actual en la pantalla

        pygame.display.update()  # Actualizar la pantalla

        # Crear rectángulos de colisión
        cabeza_rect = pygame.Rect(x1, y1, tamano_bloque, tamano_bloque)  # Rectángulo de colisión para la cabeza de la serpiente
        comida_rect = pygame.Rect(comida_x, comida_y, tamano_bloque, tamano_bloque)  # Rectángulo de colisión para la comida

        if cabeza_rect.colliderect(comida_rect):
            comida_x = round(random.randrange(0, ancho_pantalla - tamano_bloque) / tamano_bloque) * tamano_bloque  # Nueva posición X aleatoria de la comida
            comida_y = round(random.randrange(0, alto_pantalla - tamano_bloque) / tamano_bloque) * tamano_bloque  # Nueva posición Y aleatoria de la comida
            longitud_serpiente += 1  # Aumentar la longitud de la serpiente

        reloj.tick(velocidad_serpiente)  # Controlar la velocidad del juego

    pygame.quit()  # Salir de Pygame
    sys.exit()  # Salir del programa

juego()  # Iniciar el juego
