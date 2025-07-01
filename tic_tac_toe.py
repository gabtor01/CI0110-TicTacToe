'''
Desarrollador: Gabriel Torres G.
GitHub: gabtor01

Notas: 
    1) Los parámetros y los retornos de las funciones especifican
    el tipo de datos. Esto es soportado a partir de Python 3.5
    y se implementó para que el código sea más legible.

    2) Para ejecutar en la terminal, usar: python .\tic_tac_toe.py
'''

# Importar métodos de bibliotecas
from platform import processor as plt_processor, system as plt_system
from random import choice as rnd_choice
from os import system as os_system

# Variables globales de formato
ESPACIO_FONDO: str = ' ' * 61
BORDE_VENTANA: str = '─' * 61

# Definir funciones
def imprimir_menu() -> str:
    '''Muestra la pantalla principal del juego con las opciones para el
       jugador. Solicita y retorna la elección del jugador.'''

    print('\n')
    print('╭' + BORDE_VENTANA + '╮')
    print('│' + ' '*25 + negrita("TIC TAC TOE") + ' '*25 + '│')
    print('├' + BORDE_VENTANA + '┤')
    print("│ Escribe una letra:  ▄▄     ▄▄  ▄▄▄▄▄▄  ▄▄     ▄▄  ▄▄▄▄▄▄    │")
    print("│  > [j] Jugar          ▀▄ ▄▀   █      █   ▀▄ ▄▀   █      █   │")
    print("│  > [i] Instrucciones    █    █        █    █    █        █  │")
    print("│  > [c] Créditos       ▄▀ ▀▄   █      █   ▄▀ ▀▄   █      █   │")
    print("│  > [s] Salir        ▀▀     ▀▀  ▀▀▀▀▀▀  ▀▀     ▀▀  ▀▀▀▀▀▀    │")
    print('╰' + BORDE_VENTANA + '╯')

    # Manejo de excepciones para que el usuario pueda elegir en el menú
    caracter_es_valido = False
    caracteres_validos = "jics"
    while (not caracter_es_valido):
        opcion_menu = input(">>> ")
        if (len(opcion_menu) != 1):
            comentar("izquierda",
                    "¡Woah! Solo necesitas escribir una letra.",
                    "ᕙ(;∩_∩)")
        elif (opcion_menu not in caracteres_validos):
            comentar("derecha",
                    "¡Ups! Parece que esa letra no está en las opciones.",
                    "(∩_∩;)ᕗ")
        else:
            caracter_es_valido = True
    if (not caracter_es_valido):
        opcion_menu = input(">>> ")

    return opcion_menu


def imprimir_instrucciones() -> str:
    '''Muestra las instruccionbes del juego. Solicita y retorna '<' para
       que el jugador pueda regresar al menú.'''

    print('\n')
    print('╭' + BORDE_VENTANA + '╮')
    print("│{:^69}│".format(negrita("INSTRUCCIONES")))
    print('├' + BORDE_VENTANA + '┤')
    print("│  > Puedes cambiar de pantalla ingresando un caracter.       │")
    print("│  > Escribiendo [<] regresas al inicio, si no estás jugando. │")
    print("│  > Al iniciar una partida debes ingresar tu nombre y marca. │")
    print("│  >                                                          │")
    print("│  > El tablero es de 8x8 casillas, todas vacías al inicio.   │")
    print("│  > ¡Juegas contra tu computadora!                           │")
    print("│  > Las marcas seguidas en horizontal, vertical o diagonal.  │")
    print("│  > El juego utiliza turnos ¡Tú siempre comenzarás!          │")
    print("│  > Luego de cada [>>>] es donde puedes escribir.            │")
    print("│  > Las líneas válidas horizontal, vertical o diagonal.      │")
    print(r"│  > Gana quien logre primero 4 marcas en línea.      (\_/)   │")
    print("│  > Empate si el tablero se llena sin ganador.       (oᴥo)   │")
    print(r"│  > Luego de cada partida puedes iniciar otra.       /⊃ ⊂\   │")
    print("│  > Con [y] inicias otra, sino el juego termina.    ▐▀▀▀▀▀▌  │")
    print('╰' + BORDE_VENTANA + '╯')

    # Manejo de excepciones para que el usuario pueda regresar al menú
    caracter_es_valido = False

    while (not caracter_es_valido):
        volver_al_menu = input(">>> ")
        if (len(volver_al_menu) != 1):
            comentar("izquierda",
                    "¡Woah! Para volver solo escribe el caracter [<].",
                    "ᕙ(;∩_∩)")
        elif (volver_al_menu != '<'):
            comentar("derecha",
                    "¡Ups! Caracter equivado, intenta otra vez.",
                    "(∩_∩;)ᕗ")
        else:
            caracter_es_valido = True
    if (not caracter_es_valido):
        volver_al_menu = input(">>> ")

    return volver_al_menu


def imprimir_creditos() -> str:
    '''Muestra los créditos del juego. Pide y retorna '<' para que el
       jugador pueda regresar al menú.'''

    print('\n')
    print('╭' + BORDE_VENTANA + '╮')
    print("│{:^69}│".format(negrita("DESARROLLADOR")))
    print('├' + BORDE_VENTANA + '┤')
    print('│' + ESPACIO_FONDO + '│')
    print("│                      Gabriel Torres G.             * ✧ ･    │")
    print(r"│                                                 ･ﾟ (\_/)✧   │")
    print("│                      GitHub: gabtor01            * (^ᴥ^) :  │")
    print(r"│                                                    /⊃ ⊂\    │")
    print("│                                                  ▐▀▀▀▀▀▀▀▌  │")
    print('╰' + BORDE_VENTANA + '╯')

    # Manejo de excepciones para que el usuario pueda regresar al menú
    caracter_valido = False

    while (not caracter_valido):
        volver_al_menu = input(">>> ")
        if (len(volver_al_menu) != 1):
            comentar("izquierda",
                    "¡Woah! Para volver solo escribe el caracter [<].",
                    "ᕙ(;∩_∩)")
        elif (volver_al_menu != '<'):
            comentar("derecha",
                    "¡Ups! Caracter equivado, intenta otra vez.",
                    "(∩_∩;)ᕗ")
        else:
            caracter_valido = True
    if (not caracter_valido):
        volver_al_menu = input(">>> ")

    return volver_al_menu


def imprimir_tablero(tablero: dict[tuple[str, int], str],
                    nombre_jugador: str, 
                    nombre_computadora: str) -> None:
    '''Muestra el tablero del juego actualizado.'''

    columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    filas = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Imprimir el inicio de la interfaz
    # {:^30} centra la variable en un espacio de 30 caracteres
    print('\n')
    print("╭──────────────────────────────┬──────────────────────────────╮")
    print("│{:^38}│{:^38}│"
          .format(negrita(nombre_jugador), negrita(nombre_computadora)))
    print("├──────────────────────────────┴──────────────────────────────┤")
    print('│' + ESPACIO_FONDO + '│')
    print("│         " + "     ".join(columnas) + "         │")
    print("│      ╔" + "═════╦" * 7 + "═════╗      │")

    # Imprimir el cuerpo del tablero
    for fila in filas:
        # Imprimir el número de fila e inicio de celda
        print("│    {} ║".format(fila), end="") # No hacer \n al final

        # Imprimir cada marca de la fila para cada columna
        for columna in columnas:
            # No hacer \n luego de cada marca
            print("{:^5}║".format(tablero[(columna, fila)]), end="")

        # Cierre de la fila
        print(" {}    │".format(fila)) # Hacer \n porque empieza otra fila

        # Después de cada fila completada se imprime la "entrefila"
        if fila < 8:
            print("│      ╠" + "═════╬" * 7 + "═════╣      │")
        # En la octava fila se imprime el borde inferior
        else:
            print("│      ╚" + "═════╩" * 7 + "═════╝      │")

    # Imprimir el brode de la interfaz
    print("│         " + "     ".join(columnas) + "         │")
    print('│' + ESPACIO_FONDO + '│')
    print('╰' + BORDE_VENTANA + '╯')


def crear_tablero() -> dict[tuple[str, int], str]:
    '''Crea e inicializa el tablero del juego con caracteres vacíos ' '
       al comienzo de cada partida.'''
    
    # Algoritmo para crear el tablero basado en un diccionario
    columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    filas = [1, 2, 3, 4, 5, 6, 7, 8]
    tablero = {}

    # Asignar un valor inicial a todas las filas por cada columna
    for i in columnas:
        for j in filas:
            tablero[(i, j)] = ' ' 

    return tablero


def solicitar_datos() -> tuple[dict[str, str], dict[str, str]]:
    '''Agrupa los datos del jugdor y genera los respectivos datos de la
       computadora.'''
    
    info_jugador = {"nombre":"", "marca":""}
    info_computadora = {"nombre":plt_processor()[0:29], "marca":""}

    # Solicitar el nombre
    comentar("izquierda",
            "Lord {} exige saber el nombre de su contrincante..."\
            .format(info_computadora["nombre"]),
            "(╯°д°)╯︵ ┻━┻")
    
    # Manejo de excepciones para el nombre del jugador
    nombre_valido = False
    while (not nombre_valido):
        nombre_jugador = input(">>> ")
        if (len(nombre_jugador) < 31):
            # Si tiene 30 o menos caracteres es válido
            info_jugador["nombre"] = nombre_jugador
            nombre_valido = True
        else:
            comentar("izquierda",
                    "Muuucho texto... al poderoso {} le aburre"\
                    .format(info_computadora["nombre"]),
                    "(￣ρ￣)zzZZ")
            
    # Solicitar la marca
    comentar("izquierda",
            "{} ¡Ese nombre suena a victoria!"\
            .format(info_jugador["nombre"]),
            "(๑˃ᴗ˂)づ")
    
    comentar("derecha",
            "Solo falta que decidas tu marca ¿[O] || [X]?",
            "ᕙ(⇀ᴗ↼‶)ᕗ")
    
    # Manejo de excepciones para la marca del jugador
    marca_valida = False
    while (not marca_valida):
        marca_jugador = input(">>> ").upper() # No sensible a minúsculas
        if (marca_jugador == 'X' or marca_jugador == 'O'):
            # Cualquier otro caracter no es válido
            info_jugador["marca"] = marca_jugador
            marca_valida = True
        else:
            comentar("izquierda",
                "¡Solo puedes escoger entre [O] y [X] {}!"\
                .format(info_jugador["nombre"]),
                "ᕙ(;∩_∩)")

    # Definir la marca de la computadora
    if info_jugador["marca"] == 'O':
        info_computadora["marca"] = 'X'
    else:
        info_computadora["marca"] = 'O'

    return info_jugador, info_computadora


def computadora_responde(tablero: dict[tuple, str]) -> str: 
    '''Genera la jugada con la que la computadora contraataca.'''

    columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    filas = [1, 2, 3, 4, 5, 6, 7, 8]

    # Generar jugadas hasta que la celda no esté ocupada
    ubicacion_valida = False
    while (not ubicacion_valida):
        respuesta_computadora = (rnd_choice(columnas), rnd_choice(filas))
        if tablero[respuesta_computadora] == ' ':
            ubicacion_valida = True
    return "{}{}".format(respuesta_computadora[0], respuesta_computadora[1])


def colocar_marca(marca: str, 
                 posicion_marca: str, 
                 tablero: dict[tuple[str, str], str]) \
                 -> dict[tuple[str, str], str]:
    '''Ubica la marca en el tablero en la posición especificada.'''
    
    # posicion_marca[0]: columna
    # posicion_marca[1]: fila
    # .upper() para quitar sensibilidad a minúsculas
    # Castear la fila porque el tablero se crea con enteros

    # Manejo de excepciones para ubicar la marca en el tablero
    ubicacion_valida = False
    while (not ubicacion_valida):
        if (len(posicion_marca) != 2):
            comentar("izquierda",
                    "¡Woah! Solo necesitas una letra y un número.",
                    "ᕙ(;∩_∩)")       
        else:
            try:
                columna = posicion_marca[0].upper()
                fila = int(posicion_marca[1])
                coordenadas = (columna, fila)

                if (coordenadas not in tablero):
                    comentar("derecha",
                            "No existe esa ubicación en nuestro tablero...",
                            "(U_U')")
                elif (tablero[coordenadas] != ' '):
                    comentar("izquierda",
                            "Ya existe una marca en esa posición...",
                            "(U_U')") 
                else:
                    ubicacion_valida = True
            except ValueError:
                comentar("derecha",
                        "¡Ups! La fila debe ser un número entero del 1 al 8.",
                        "(∩_∩;)ᕗ")
        if (not ubicacion_valida):
            posicion_marca = input(">>> ")

    tablero[coordenadas] = marca
    return tablero


def hay_ganador(tablero: dict[tuple[str, str], str]) -> bool:
    '''Implementa un algoritmo de búsqueda para hallar los patrones de 4
       coincidencias de la misma marca 'X' u 'O' en horizontal, vertical
       o diagonal.'''

    # Acceder a la columna con columnas[i]
    columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    # El tablero es 8x8
    n = 8

    # Direcciones para recorrer el tablero según cada patrón
    direcciones = [
        (1,  0), # Hori(─): 1 col a la derecha, no se mueve la fila
        (0,  1), # Vert(|): 1 fila abajo, no se mueve la col
        (1,  1), # Diag(\): 1 fila abajo y 1 col a la derecha
        (1, -1)  # Diag(/): 1 fila arriba y 1 col a la derecha
    ]

    for i in range(n):
        for j in range(1, n + 1):
            # Obtener llave actual
            coordenadas = (columnas[i], j)

            # Obtener valor actual en llave actual
            marca_act = tablero[coordenadas]

            # Si la marca no es ni X ni O, saltar a siguiente iteración
            if marca_act == ' ':
                continue

            for (mov_colu, mov_fila) in direcciones:
                hay_ganador = True

                # Recorrer 3 marcas desde la marca actual
                for k in range(1, 4):
                    sig_colu = i + mov_colu * k
                    sig_fila = j + mov_fila * k
                    
                    # Si los índices se salen de rango, no se continúa
                    if not (0 <= sig_colu < n and 1 <= sig_fila <= n):
                        hay_ganador = False
                        break
                    
                    # Si se rompe el patrón de 4, no se continúa
                    if tablero[(columnas[sig_colu], sig_fila)] != marca_act:
                        hay_ganador = False
                        break

                if hay_ganador:
                    return True

    return False


def limpiar_consola() -> None:
    '''Borra el texto que se ha impreso en la consola.'''
    # Seleccionar comando según el sistema operativo
    if plt_system() == 'Windows':
        os_system('cls')
    else:
        os_system('clear')


def negrita(texto: str) -> str:
    '''Aplica negrita a la cadena utilizada como
       parámetro usando códigos de escape ANSI.'''
    return "\033[1m"+texto+"\033[0m"


def comentar(lateralidad: str,
             mensaje: str,
             carita: str) -> None:
    '''Da formato a los comentarios que el jugdor ve
       en diferentes momentos durante la partida.'''

    if (lateralidad == "izquierda"):
        print("\n")
        print("  ╭─────────────────────────────────────────────────────────╮")
        print("  │{:^65}│".format(negrita(mensaje)))
        print("  │╭────────────────────────────────────────────────────────╯")
        print("  ╰╯")
        print(carita)
        print("\n")
    elif (lateralidad == "derecha"):
        print("\n")
        print("  ╭─────────────────────────────────────────────────────────╮")
        print("  │{:^65}│".format(negrita(mensaje)))
        print("  ╰────────────────────────────────────────────────────────╮│")
        print("                                                           ╰╯")
        print(' ' * 57 +carita)
        print("\n")


# Flujo del juego
opcion_menu = ' '
while (opcion_menu != 's'):
    opcion_menu = imprimir_menu()

    if (opcion_menu == 'i'):
        limpiar_consola()
        regresar_menu = imprimir_instrucciones()
        if (regresar_menu == '<'):
            limpiar_consola()

    elif (opcion_menu == 'c'):
        limpiar_consola()
        regresar_menu = imprimir_creditos()
        if (regresar_menu == "<"):
            limpiar_consola()

    elif (opcion_menu == 'j'):
        limpiar_consola()

        # Solicitar datos al jugador
        datos_jugador, datos_computadora = solicitar_datos()

        # Crear el tablero e inicializar valores de las claves en ' '
        tablero_juego = crear_tablero()

        # Control del juego
        contador_turnos = 1
        while (contador_turnos != 64):
            # Empieza el jugador

            # Mostrar el tablero
            limpiar_consola()
            imprimir_tablero(tablero_juego,
                             datos_jugador["nombre"],
                             datos_computadora["nombre"])

            # Solicitar la jugada 
            ubicacion_marca = input(">>> ")
            tablero_juego = colocar_marca(datos_jugador["marca"],
                                          ubicacion_marca, 
                                          tablero_juego)
            
            contador_turnos += 1
            if (contador_turnos > 6 and 
                hay_ganador(tablero_juego)):
                    limpiar_consola()
                    imprimir_tablero(tablero_juego,
                                datos_jugador["nombre"],
                                datos_computadora["nombre"])

                    comentar("izquierda",
                            "¡Has ganado {}!"\
                            .format(datos_jugador["nombre"]),
                            "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
 
                    break # Si hay ganador se rompe el ciclo

            # Mostrar el tablero
            limpiar_consola()
            imprimir_tablero(tablero_juego, 
                             datos_jugador["nombre"],
                             datos_computadora["nombre"])
            
            # Turno de la computadora

            # Generar la jugada
            ubicacion_marca = computadora_responde(tablero_juego)
            colocar_marca(datos_computadora["marca"],
                          ubicacion_marca,
                          tablero_juego)

            contador_turnos += 1
            if (contador_turnos > 7 and 
                hay_ganador(tablero_juego)):
                    limpiar_consola()
                    imprimir_tablero(tablero_juego,
                                datos_jugador["nombre"],
                                datos_computadora["nombre"])
                    
                    comentar("izquierda",
                            "{} te ha derrotado..."\
                            .format(datos_computadora["nombre"]),
                            "(╥﹏╥)")
                    break

        # Si se acaban los turnos y no hubo ganador es un empate
        if (not hay_ganador(tablero_juego)):
            limpiar_consola()
            comentar("izquierda",
                    "¿Ha sido empate? Lo creía imposible.",
                    "(￣～￣;)")

    else:
        limpiar_consola()
        comentar("izquierda",
                "¡Hasta pronto!",
                "(∩_∩)ノ")