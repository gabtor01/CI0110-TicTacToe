'''
Desarrollador: Gabriel Torres G.
GitHub: gabtor01

Notas: 
    1) Los parámetros y los retornos de las funciones especifican
    el tipo de datos. Esto es soportado a partir de Python 3.5
    y se implementó para que el código sea más legible.

    2) Para ejecutar en la terminal, usar: python .\tic_tac_toe.py
'''

# Importar bibliotecas útiles
import platform
import random

# Definir funciones
def imprimir_menu() -> str:
    '''Muestra la pantalla principal del juego con las opciones para el
       jugador. Solicita y retorna la elección del jugador.'''
    
    print("╭─────────────────────────────────────────────────────────────╮")
    print("│                         TIC TAC TOE                         │")
    print("├─────────────────────────────────────────────────────────────┤")
    print("│ Escribe una letra:  ▄▄     ▄▄  ▄▄▄▄▄▄  ▄▄     ▄▄  ▄▄▄▄▄▄    │")
    print("│  > [j] Jugar          ▀▄ ▄▀   █      █   ▀▄ ▄▀   █      █   │")
    print("│  > [i] Instrucciones    █    █        █    █    █        █  │")
    print("│  > [c] Créditos       ▄▀ ▀▄   █      █   ▄▀ ▀▄   █      █   │")
    print("│  > [s] Salir        ▀▀     ▀▀  ▀▀▀▀▀▀  ▀▀     ▀▀  ▀▀▀▀▀▀    │")
    print("╰─────────────────────────────────────────────────────────────╯")
    # Recordar agregar manejo de execpciones
    opcion_menu = input(">>> ")
    return opcion_menu


def imprimir_instrucciones() -> str:
    '''Muestra las instruccionbes del juego. Solicita y retorna '<' para
       que el jugador pueda regresar al menú.'''

    print("╭─────────────────────────────────────────────────────────────╮")
    print("│                        INSTRUCCIONES                        │")
    print("├─────────────────────────────────────────────────────────────┤")
    print("│  >                                                          │")
    print("│  >                                                          │")
    print("│  >                                                          │")
    print("│  >                                                          │")
    print("│  >                                                          │")
    print("│  >                                                          │")
    print("│  >                                                          │")
    print("│  >                                                          │")
    print("│  > Luego de cada [>>>] es donde puedes escribir.            │")
    print("│  > Escribiendo [<] regresas al inicio, si no estás jugando. │")
    print("╰─────────────────────────────────────────────────────────────╯")
    # Recordar agregar manejo de execpciones y terminar de agregar instrucciones
    volver_menu = input(">>> ")
    return volver_menu


def imprimir_creditos() -> str:
    '''Muestra los créditos del juego. Pide y retorna '<' para que el
       jugador pueda regresar al menú.'''

    print("╭─────────────────────────────────────────────────────────────╮")
    print("│                        DESARROLLADOR                        │")
    print("├─────────────────────────────────────────────────────────────┤")
    print("│                                                             │")
    print("│                      Gabriel Torres G.                      │")
    print("│                                                   * ✧ ･     │")
    print(r"│                      GitHub: gabtor01          ･ﾟ (\_/)✧    │")
    print("│                                                 * (^ᴥ^) :   │")
    print(r"│                                                   /⊃ ⊂\     │")
    print("│                                                 ▐▀▀▀▀▀▀▀▌   │")
    print("╰─────────────────────────────────────────────────────────────╯")
    # Recordar agregar manejo de execpciones
    volver_menu = input(">>> ")
    return volver_menu


def imprimir_tablero(tablero: dict[tuple, str],
                     nombre_jugador: str, 
                     nombre_computadora: str) -> None:
    '''Muestra el tablero del juego actualizado.'''

    columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    filas = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Imprimir el inicio de la interfaz
    # {:^30} centra la variable en un espacio de 30 caracteres
    print("╭──────────────────────────────┬──────────────────────────────╮")
    print("│{:^30}│{:^30}│".format(nombre_jugador, nombre_computadora))
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
    print("│                                                             │")
    print("╰─────────────────────────────────────────────────────────────╯")


def crear_tablero() -> dict[tuple, str]:
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
       computadora. Se usan códigos de escape ANSI en la impresión para
       dar formato a los nombres.'''
    
    info_jugador = {"nombre":"", "marca":""}
    info_computadora = {"nombre":platform.processor()[0:7], "marca":""}

    # Solicitar el nombre
    print("\nLord \033[1m{}\033[0m exige saber el nombre de su contrincante... "
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
    print("\n(๑˃ᴗ˂)づ \033[1m{}\033[0m, solo falta que decidas tu marca "
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
        respuesta_computadora = (random.choice(columnas), random.choice(filas))
        if tablero[respuesta_computadora] == ' ':
            ubicacion_valida = True
    return "{}{}".format(respuesta_computadora[0], respuesta_computadora[1])


def colocar_marca(marca: str, 
                  posicion_marca: str, 
                  tablero: dict[tuple, str]) -> dict[tuple, str]:
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
        if not ubicacion_valida:
            posicion_marca = input(">>> ")

    tablero[coordenadas] = marca
    return tablero


def buscar_ganador(tablero: dict[tuple, str]) -> None:
    '''Implementa un algoritmo de búsqueda para hallar los patrones de 4
       coincidencias de la misma marca 'X' u 'O' en horizontal, vertical
       o diagonal.'''
    # Por hacer
    # Recordar revisar algoritmo de ventana deslizante


opcion_menu = ' '
# Invocar funciones según el flujo del juego
while (opcion_menu != 's'):
    opcion_menu = imprimir_menu()

    if (opcion_menu == 'i'):
        regresar_menu = imprimir_instrucciones()
        if (regresar_menu == '<'):
            continue

    elif (opcion_menu == 'c'):
        regresar_menu = imprimir_creditos()
        if (regresar_menu == "<"):
            continue

    elif (opcion_menu == 'j'):
        # Crear el tablero e inicializar valores de las claves en ' '
        tablero_juego = crear_tablero()

        # Solicitar datos al jugador
        datos_jugador, datos_computadora = solicitar_datos()

        # Controlar los turnos
        for i in range(0, 32):
            # Turno del jugador

            # Mostrar el tablero
            imprimir_tablero(tablero_juego,
                             datos_jugador["nombre"],
                             datos_computadora["nombre"])

            # Solicitar la jugada 
            ubicacion_marca = input(">>> ")
            tablero_juego = colocar_marca(datos_jugador["marca"],
                                          ubicacion_marca, 
                                          tablero_juego)

            # Mostrar el tablero
            imprimir_tablero(tablero_juego, 
                             datos_jugador["nombre"],
                             datos_computadora["nombre"])
            
            # Turno de la computadora

            # Generar la jugada
            ubicacion_marca = computadora_responde(tablero_juego)
            colocar_marca(datos_computadora["marca"],
                          ubicacion_marca,
                          tablero_juego)

    else:
        print("Parece que esa opción no está dentro del juego (╥﹏╥)")
        