# Desarrollador: Gabriel Torres Garbanzo

# Importación de librerías útiles
import platform as plt
import random as rnd

# Definición de métodos
def imprimir_menu():
    '''Esta función se utiliza para mostrar en formato de texto
        la pantalla principal del juego Tic Tac Toe en donde se
        muestran las opciones al jugador.

        > Entradas:   ninguna
        > Retornos:   ninguno'''
    
    print("Esta es la pantalla principal")


def imprimir_instrucciones():
    '''Esta función se utiliza para mostrar en formato de texto
        las instruccionbes del juego Tic Tac Toe.

        > Entradas:   ninguna
        > Retornos:   ninguno'''
    
    print("Estas son las instrucciones")


def imprimir_creditos():
    '''Esta función se utiliza para mostrar en formato de texto
        los créditos del juego Tic Tac Toe.

        > Entradas:   ninguna
        > Retornos:   ninguno'''
    
    print("Estos son los creditos")


def imprimir_tablero(matriz_tablero):
    '''Esta función se utiliza para mostrar el tablero del juego
        con el formato de un tablero de juego de mesa.

        > Entradas: diccionario matriz_tablero
        > Retornos:   ninguno'''
    
    # Recorrer el tablero y agregar formato cuando se imprime
    print(matriz_tablero)


def inicializar_tablero(matriz_tablero):
    '''Esta función se utiliza para llenar el tablero del juego
        con caracteres vaíos " " al inicio de cada partida.
        
        > Entradas:   diccionario matriz_tablero
        > Retornos:   diccionario matriz_tablero'''

    return matriz_tablero


def computadora_piensa(matriz_tablero):
    '''Esta función se utiliza para generar la jugada con la que
        la computadora contraataca.

        > Entradas:   diccionario matriz_tablero
        > Retornos:   string      jugada_computadora'''
    
    jugada_computadora = ""
    return jugada_computadora


def jugar(cadena_jugada):
    '''Esta función se utiliza para aplicar la jugada que el humano
        o la computadora aplican en su respectivo turno. Una vez se
        coloca la marca se retorna el tablero modificado.

        > Entradas:   string       cadena_jugada
        > Retornos:   diccionario  tablero'''
    
    return tablero


def buscar_ganador(matriz_tablero):
    '''Esta función implementa el algoritmo de búsqueda con
        el que se buscan patrones de 4 de la misma marca "X" 
        u "O" en línea horizontal, vertical o diagonal.

        > Entradas:   diccionario matriz_tablero
        > Retornos:   ninguno'''
    
    print("Empate")


def obtener_nombre_computadora():
    '''Esta función se utiliza para extraer el nombre del
        CPU de la computadora donde se ejecute el juego.

        > Entradas:   ninguna
        > Retornos:   string nombre_CPU'''
    
    nombre_CPU = ""
    return nombre_CPU


# Definición e inicialización de variables globales
jugada = ""
datos_jugador = {"nombre":"", "marca_juego":"", "jugada":jugada}
datos_computadora = {"nombre":obtener_nombre_computadora(), "marca_juego":"", "jugada":jugada}
opcion_menu = ""
regresar_menu = ""
tablero = {}

# Juego como tal
while (opcion_menu != "s"):
    imprimir_menu()
    opcion_menu = input(("\nElige una opción: "))

    if (opcion_menu == "i"):
        imprimir_instrucciones()
        regresar_menu = input("Ingresa \"<\" para regresar: ")

        if (regresar_menu == "<"):
            imprimir_menu()
            opcion_menu = input(("\nElige una opción: "))

    elif (opcion_menu == "c"):
        imprimir_creditos()
        regresar_menu = input("Ingresa \"<\" para regresar: ")

        if (regresar_menu == "<"):
            imprimir_menu()
            opcion_menu = input(("\nElige una opción: "))

    elif (opcion_menu == "j"):
        # Aqui se desarrolla el algoritmo del juego
        for i in range(0, 64):
            imprimir_tablero()
    else:
        print("Parece que esa opción aún no está dentro del juego :(")
        