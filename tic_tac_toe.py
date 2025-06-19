'''
Desarrollador: Gabriel Torres G.
Github: gabtor01

Nota: los parámetros y los retornos de las funciones especifican
      el tipo de datos. Esto es soportado a partir de Python 3.5
      y se implementa para que el código sea más legible.
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
    print("│  > Luego de cada [>>>] es donde debes escribir.             │")
    print("│  > Escribiendo [<] regresas al inicio, si no estás jugando. │")
    print("╰─────────────────────────────────────────────────────────────╯")
    # Recordar agregar manejo de execpciones
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
    print(r"│                      Github: gabtor01          ･ﾟ (\_/)✧    │")
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
    
    # Imprimir el inicio del tablero
    print("╭──────────────────────────────┬──────────────────────────────╮")
    print("│{:^30}│{:^30}│".format(nombre_jugador, nombre_computadora))
    print("├──────────────────────────────┴──────────────────────────────┤")
    print("│                                                             │")
    print("│         " + "     ".join(columnas) + "         │")
    print("│      ╔" + "═════╦" * 7 + "═════╗      │")

    # Imprimir el cuerpo del tablero
    for fila in range(1, 9):
        celdas = [] # Por cada fila almacena 8 marcas (Una por columna)
        for columna in columnas:
            celdas.append(tablero[(columna, fila)])

        print("│    {} ║{:^5}║{:^5}║{:^5}║{:^5}║{:^5}║{:^5}║{:^5}║{:^5}║ {}    │"
            .format(fila, *celdas, fila))

        if fila < 8:
            print("│      ╠" + "═════╬" * 7 + "═════╣      │")
        else:
            print("│      ╚" + "═════╩" * 7 + "═════╝      │")

    # Fin del tablero
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
    '''Solicita los datos (Nombre y marca) del jugdor al inicio de la
       partida y genera los respectivos datos de la computadora.'''
    
    info_jugador = {"nombre":"", "marca":""}
    info_computadora = {"nombre":platform.processor()[0:26], "marca":""}

    # Nombre
    print("\n\033[1;3m{}\033[0m exige saber el nombre de su contrincante... "
          "(╯°д°)╯︵ ┻━┻\n ".format(info_computadora["nombre"]))
    info_jugador["nombre"] = input(">>> ")

    # Marcas
    print("\n(๑˃ᴗ˂)づ \033[1;3m{}\033[0m, solo falta decidir tu marca "
          "¿[O] ᕙ(⇀ᴗ↼‶)ᕗ [X]?\n".format(info_jugador["nombre"]))
    info_jugador["marca"] = input(">>> ")

    if info_jugador["marca"] == "O":
        info_computadora["marca"] = "X"
    else:
        info_computadora["marca"] = "O"

    return (info_jugador, info_computadora)


def computadora_responde(tablero: dict[tuple, str]) -> str: 
    '''Genera la jugada con la que la computadora contraataca.'''

    columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    filas = filas = [1, 2, 3, 4, 5, 6, 7, 8]

    # Generar jugadas hasta que la celda no esté ocupada
    while True:
        colu = random.choice(columnas)
        fila = random.choice(filas)

        if tablero[(colu, fila)] == ' ':
            return "{} + {}".format(colu, fila)


def colocar_marca(marca: str, cadena_jugada: str) -> dict[tuple, str]:
    '''Aplica la jugada que el humano o la computadora generan en su
       respectivo turno.'''
    
    # cadena_jugada[0] -> columna
    # cadena_jugada[1] -> fila
    coordenadas = (cadena_jugada[0], cadena_jugada[1])

    tablero[coordenadas] = marca if tablero[coordenadas] == " " else \
                           print("Ya existe una marca en esa posición :(\n")
    
    return tablero


def buscar_ganador(tablero: dict[tuple, str]) -> None:
    '''Implementa un algoritmo de búsqueda para hallar los patrones de 4
       coincidencias de la misma marca "O" o "X" en horizontal, vertical
       o diagonal.'''
    # Por hacer
    # Tratar de implementar algoritmo de ventana deslizante



# Llamar funciones según el flujo del juego
while (opcion_menu != "s"):
    opcion_menu = imprimir_menu()

    if (opcion_menu == "i"):
        imprimir_instrucciones()
        regresar_menu = input("Digite \"<\" para regresar: ")

        if (regresar_menu == "<"):
            imprimir_menu()
            opcion_menu = input(("\nElige una opción: "))

    elif (opcion_menu == "c"):
        imprimir_creditos()
        regresar_menu = input("Digite \"<\" para regresar: ")

        if (regresar_menu == "<"):
            imprimir_menu()
            opcion_menu = input(("\nElige una opción: "))

    elif (opcion_menu == "j"):
        # crear e inicializar el tablero
        tablero = crear_tablero()

        # Solicitar el nombre al usuario
        datos_jugador, datos_computadora = solicitar_datos()

        for i in range(0, 32):
            # Mostrar el tablero
            imprimir_tablero()

            # Pedir la jugada del humano y colocarla en el tablero
            datos_jugador["jugada"] = input("Define tu jugada {}: ".format(datos_jugador["nombre"]))
            colocar_marca(datos_jugador["jugada"])

            # Mostrar el tablero nuevamente "para la computadora"
            imprimir_tablero()

            # Generar la jugada de la computadora y colocarla en el tablero
            datos_computadora["jugada"] = computadora_piensa(tablero)
            colocar_marca(datos_computadora["jugada"])

    else:
        print("Parece que esa opción aún no está dentro del juego :(")
        