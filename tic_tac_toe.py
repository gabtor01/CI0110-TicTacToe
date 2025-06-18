'''Desarrollador: Gabriel Torres Garbanzo
   
'''

# Importación de bibliotecas útiles
import platform
import random

# Definición de métodos
def imprimir_menu() -> str:
    '''Muestra en formato de texto la pantalla principal del juego  con
       las opciones para el jugador.'''
    
    print("╭─────────────────────────────────────────────────────────────╮")
    print("│                         TIC TAC TOE                         │")
    print("├─────────────────────────────────────────────────────────────┤")
    print("│ Escribe una letra:  ▄▄     ▄▄  ▄▄▄▄▄▄  ▄▄     ▄▄  ▄▄▄▄▄▄    │")
    print("│  > [j] Jugar          ▀▄ ▄▀   █      █   ▀▄ ▄▀   █      █   │")
    print("│  > [i] Instrucciones    █    ▐        ▌    █    ▐        ▌  │")
    print("│  > [c] Créditos       ▄▀ ▀▄   █      █   ▄▀ ▀▄   █      █   │")
    print("│  > [s] Salir        ▀▀     ▀▀  ▀▀▀▀▀▀  ▀▀     ▀▀  ▀▀▀▀▀▀    │")
    print("╰─────────────────────────────────────────────────────────────╯")
    opcion_menu = input(">>> ")
    return opcion_menu


def imprimir_instrucciones() -> str:
    '''Muestra en formato de texto las instruccionbes del juego.'''

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
    print("│  > Luego de [>>>] es donde debes escribir.                  │")
    print("│  > Escribiendo [<] regresas al inicio, si no estás jugando. │")
    print("╰─────────────────────────────────────────────────────────────╯")
    volver_menu = input(">>> ")

    return volver_menu


def imprimir_creditos() -> str:
    '''Muestra en formato de texto los créditos del juego.'''
    
    print("Estos son los creditos")


def imprimir_tablero(tablero: dict[tuple, str],
                     nombre_jugador: str, 
                     nombre_computadora: str) -> None:
    '''Muestra el tablero del juego en formato de texto  semejante a un
       tablero de juego de mesa.'''

    columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    
    # Inicio del tablero
    print("╭──────────────────────────────┬──────────────────────────────╮")
    print("│{:^30}│{:^30}│".format(nombre_jugador, nombre_computadora))
    print("├──────────────────────────────┴──────────────────────────────┤")
    print("│                                                             │")
    print("│         " + "     ".join(columnas) + "         │")
    print("│      ╔" + "═════╦" * 7 + "═════╗      │")

    # Datos del tablero
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
       en el comienzo de cada partida.'''
    
    # Algoritmo para crear el tablero basado en un diccionario
    columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    filas = range(1, 9)
    tablero = {}

    for i in columnas:
        for j in filas:
            tablero[(i, j)] = ' '

    return tablero


def solicitar_datos() -> tuple[dict[str, str], dict[str, str]]:
    '''Solicita que el jugador ingrese su nombre y marca al inicio de la
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


def computadora_piensa(tablero: dict[tuple, str]) -> str: 
    '''Genera la jugada con la que la computadora contraataca.'''

    columnas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    filas = range(1, 9)

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
    '''Algoritmo de búsqueda para hallar patrones de 4 coincidencias 
       de la misma marca "X" u "O" en horizontal, vertical o diagonal.
       > Entradas: dict[tuple, str] tablero
       > Retornos: None'''
    
    print("Empate")




# Juego como tal
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
        