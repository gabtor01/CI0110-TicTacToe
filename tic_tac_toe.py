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
    volver_menu = input("│                                                      >>>  │")
    print("╰─────────────────────────────────────────────────────────────╯")
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
    columnas = "ABCDEFGH"
    filas = [1,2,3,4,5,6,7,8]
    tablero = {}

    for i in columnas:
        for j in filas:
            tablero[(i, j)] = ' '

    return tablero


def computadora_piensa(tablero: dict[tuple, str]) -> str: 
    '''Genera la jugada con la que la computadora contraataca.
       > Entradas: dict[tuple, str] tablero
       > Retornos: str jugada_computadora'''

    # Caso base que la clave no este en el tablero
    # Mientras la clave no este en el tablero se sigue llamando a la funcion
    columna_aleatoria = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    fila_aleatoria = random.choice(range(1, 9))
    contra_computadora = "{} + {}".format(columna_aleatoria, fila_aleatoria)

    if (columna_aleatoria, fila_aleatoria) not in tablero:
        return contra_computadora
    else:
        computadora_piensa(tablero)


def colocar_marca(marca: str, cadena_jugada: str) -> dict[tuple, str]:
    '''Aplica la jugada que el humano o la computadora generan en 
       su respectivo turno.
       > Entradas: str marca, str cadena_jugada
       > Retornos: dict[tuple, str] tablero'''
    
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



# Definición e inicialización de variables globales
datos_jugador = {"nombre":"", "marca_juego":"", "jugada":""}
datos_computadora = {"nombre":platform.processor(), "marca_juego":"", "jugada":""}
regresar_menu = ""
tablero = {}

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

    elif (opcion_menu == "j"): # Si el usuario elige jugar
        # Inicializar el tablero al iniciar la partida
        inicializar_tablero()
        
        # Solicitar el nombre al usuario
        datos_jugador["nombre"] = input("{} quiere saber el nombre de su contrincante: \n".format(datos_computadora["nombre"]))

        # Definir las marcas
        datos_jugador["marca_juego"] = input("Escoge tu ficha {}, "" O "" o  "" X "" y buena suerte: ".format(datos_jugador["nombre"]))
        datos_computadora["marca_juego"] = "X" if datos_jugador["marca_juego"] == "O" else "O"

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
        