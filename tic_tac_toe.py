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
    print('│' + ' '*25 + "\033[1mTIC TAC TOE\033[0m" + ' '*25 + '│')
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
            print("\n¡Woah! Recuerda que solo necesitas" \
                    " escribir una letra (∩_∩;)\n")
        elif (opcion_menu not in caracteres_validos):
            print("\n¡Ups! Parece que esa letra no está" \
                    " en las opciones (∩_∩;)\n")
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
    print("│                        INSTRUCCIONES                        │")
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
            print("\n¡Woah! Recuerda que para regresar al inicio" \
                    " solo necesitas escribir [<] (∩_∩;)\n")
        elif (volver_al_menu != '<'):
            print("\n¡Ups! Parece que eso no es un [<]"\
                    " vuelve a intentarlo (∩_∩;)\n")
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
    print("│                        DESARROLLADOR                        │")
    print('├' + BORDE_VENTANA + '┤')
    print('│' + ESPACIO_FONDO + '│')
    print("│                      Gabriel Torres G.                      │")
    print("│                                                   * ✧ ･     │")
    print(r"│                      GitHub: gabtor01          ･ﾟ (\_/)✧    │")
    print("│                                                 * (^ᴥ^) :   │")
    print(r"│                                                   /⊃ ⊂\     │")
    print("│                                                 ▐▀▀▀▀▀▀▀▌   │")
    print('╰' + BORDE_VENTANA + '╯')

    # Manejo de excepciones para que el usuario pueda regresar al menú
    caracter_valido = False

    while (not caracter_valido):
        volver_al_menu = input(">>> ")
        if (len(volver_al_menu) != 1):
            print("\n¡Woah! Recuerda que para regresar al inicio" \
                    " solo necesitas escribir [<] (∩_∩;)\n")
        elif ((volver_al_menu != '<')):
            print("\n¡Ups! Parece que eso no es un [<]"\
                    " vuelve a intentarlo (∩_∩;)\n")
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
    print("│\033[1m{:^30}\033[0m│\033[1m{:^30}\033[0m│"
          .format(nombre_jugador, nombre_computadora))
    print("├──────────────────────────────┴──────────────────────────────┤")
    print("│                                                             │")
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
    info_computadora = {"nombre":plt_processor()[0:7], "marca":""}

    # Solicitar el nombre
    print("\nLord {} exige saber el nombre de su contrincante... "
          "(╯°д°)╯︵ ┻━┻\n ".format(info_computadora["nombre"]))
    
    # Manejo de excepciones para el nombre del jugador
    nombre_valido = False
    while (not nombre_valido):
        nombre_jugador = input(">>> ")
        if (len(nombre_jugador) < 31):
            # Si tiene 30 o menos caracteres es válido
            info_jugador["nombre"] = nombre_jugador
            nombre_valido = True
        else:
            print("\nMucho texto... (￣ρ￣)zzZZ\n")
            
    # Solicitar la marca
    print("\n(๑˃ᴗ˂)づ Muy bien {}, solo falta que decidas tu marca "
          "¿[O] ᕙ(⇀ᴗ↼‶)ᕗ [X]?\n".format(info_jugador["nombre"]))
    
    # Manejo de excepciones para la marca del jugador
    marca_valida = False
    while (not marca_valida):
        marca_jugador = input(">>> ").upper() # No sensible a minúsculas
        if (marca_jugador == 'X' or marca_jugador == 'O'):
            # Cualquier otro caracter no es válido
            info_jugador["marca"] = marca_jugador
            marca_valida = True
        else:
            print("\n¡Solo puedes escoger entre [O] y [X] \033[1m{}\033[0m!\n"
                  .format(info_jugador["nombre"]))

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
            print("\n¡Woah! Recuerda que solo necesitas" \
                  " 2 dígitos (∩_∩;)\n")
        else:
            try:
                columna = posicion_marca[0].upper()
                fila = int(posicion_marca[1])
                coordenadas = (columna, fila)

                if (coordenadas not in tablero):
                    print("\nNo tenemos esa ubicación en " \
                          "nuestro tablero (U_U')\n")
                elif (tablero[coordenadas] != ' '):
                    print("\nYa existe una marca en esa posición (╥﹏╥)\n")
                else:
                    ubicacion_valida = True
            except ValueError:
                print("\n¡Ups! No olvides que la fila debe" \
                      " ser un número del 1 al 8 (∩_∩;)\n")
        if (not ubicacion_valida):
            posicion_marca = input(">>> ")

    tablero[coordenadas] = marca
    return tablero


def hay_ganador(tablero: dict[tuple[str, str], str]) -> bool:
    '''Implementa un algoritmo de búsqueda para hallar los patrones de 4
       coincidencias de la misma marca 'X' u 'O' en horizontal, vertical
       o diagonal.'''

    columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']   
    n = 8  # tablero 8x8

    for i in range(0, n):
        for j in range(1, n + 1): # Filas comienzan en índice 1
            coordenadas = (columnas[i], j)
            if coordenadas not in tablero:
                continue

            marca = tablero[coordenadas]
            if marca not in ('X', 'O'):
                continue

            # Horizontal (─)
            if (i + 3 < n                            and
                tablero[(columnas[i+1], j)] == marca and 
                tablero[(columnas[i+2], j)] == marca and
                tablero[(columnas[i+3], j)] == marca):
                return True

            # Vertical (|)
            if (j + 3 <= n                               and 
                tablero.get((columnas[i], j+1)) == marca and
                tablero.get((columnas[i], j+2)) == marca and
                tablero.get((columnas[i], j+3)) == marca):
                return True

            # Diagonal (\)
            if ((i + 3 < n and j + 3 <= n)                 and
                tablero.get((columnas[i+1], j+1)) == marca and
                tablero.get((columnas[i+2], j+2)) == marca and
                tablero.get((columnas[i+3], j+3)) == marca):
                return True

            # Diagonal (/)
            if ((i + 3 < n and j - 3 >= 1)                 and
                tablero.get((columnas[i+1], j-1)) == marca and
                tablero.get((columnas[i+2], j-2)) == marca and
                tablero.get((columnas[i+3], j-3)) == marca):
                return True

    return False


def limpiar_texto() -> None:
    '''Limpia la consola según avance el juego.'''
    if plt_system() == 'Windows':
        os_system('cls')
    else:
        os_system('clear')


opcion_menu = ' '
# Control de cambio de pantallas
while (opcion_menu != 's'):
    opcion_menu = imprimir_menu()

    if (opcion_menu == 'i'):
        limpiar_texto()
        regresar_menu = imprimir_instrucciones()
        if (regresar_menu == '<'):
            limpiar_texto()
            continue

    elif (opcion_menu == 'c'):
        limpiar_texto()
        regresar_menu = imprimir_creditos()
        if (regresar_menu == "<"):
            limpiar_texto()
            continue

    elif (opcion_menu == 'j'):
        limpiar_texto()

        # Crear el tablero e inicializar valores de las claves en ' '
        tablero_juego = crear_tablero()

        # Solicitar datos al jugador
        datos_jugador, datos_computadora = solicitar_datos()

        # Control del juego
        contador_turnos = 1
        while (contador_turnos != 64):
            # Empieza el jugador

            # Mostrar el tablero
            limpiar_texto()
            imprimir_tablero(tablero_juego,
                             datos_jugador["nombre"],
                             datos_computadora["nombre"])

            # Solicitar la jugada 
            ubicacion_marca = input(">>> ")
            tablero_juego = colocar_marca(datos_jugador["marca"],
                                          ubicacion_marca, 
                                          tablero_juego)
            
            contador_turnos += 1
            if (contador_turnos > 6):
                if (hay_ganador(tablero_juego)):
                    limpiar_texto()
                    imprimir_tablero(tablero_juego,
                                datos_jugador["nombre"],
                                datos_computadora["nombre"])
                    
                    print("\n¡Has ganado {}!\n"
                        .format(datos_jugador["nombre"]))
                    break # Si hay ganador se rompe el ciclo

            # Mostrar el tablero
            limpiar_texto()
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
            if (contador_turnos > 7):
                if (hay_ganador(tablero_juego)):
                    limpiar_texto()
                    imprimir_tablero(tablero_juego,
                                datos_jugador["nombre"],
                                datos_computadora["nombre"])
                    
                    print("\n{} te ha derrotado (╥﹏╥)\n"
                        .format(datos_computadora["nombre"]))
                    break

        # Si se acaban los turnos y no hubo ganador es un empate
        if (not hay_ganador(tablero_juego)):
            limpiar_texto()
            print("\n¡Has igualado el poder de {} con un empate!\n"
                  .format(format(datos_computadora["nombre"])))

    else:
        limpiar_texto()
        print("\n")
        print("  ╭────────────────╮")
        print("  │ ¡Hasta pronto! │")
        print("  │╭───────────────╯")
        print("  ╰╯                ")
        print("(∩_∩)ノ")
        print("\n")
