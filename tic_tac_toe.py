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
    '''Esta función se utiliza para crear y llenar el tablero 
        del juego con caracteres vaíos " " al inicio de cada 
        partida.
        
        > Entradas:   diccionario matriz_tablero
        > Retornos:   diccionario matriz_tablero'''
    
    # Algoritmo para crear un tablero basado en un diccionario
    columnas = "ABCDEFGH"
    filas = [1,2,3,4,5,6,7,8]
    for i in range(0, 8):
        for j in range(0, 8):
            matriz_tablero = {(columnas[i], filas[j]) : " "}

    return matriz_tablero


def computadora_piensa(matriz_tablero):
    '''Esta función se utiliza para generar la jugada con la que
        la computadora contraataca.

        > Entradas:   diccionario matriz_tablero
        > Retornos:   string      jugada_computadora'''
    
    contraataque_computadora = ""
    return contraataque_computadora


def colocar_marca(marca, cadena_jugada):
    '''Esta función se utiliza para aplicar la jugada que el humano
        o la computadora generan en su respectivo turno. Una vez se
        coloca la marca se retorna el tablero modificado.

        > Entradas:   string       cadena_jugada
        > Retornos:   diccionario  tablero'''
    
    # cadena_jugada[0] -> columna
    # cadena_jugada[1] -> fila
    coordenadas = (cadena_jugada[0], cadena_jugada[1])

    tablero[coordenadas] = marca if tablero[coordenadas] == " " else print("Ya existe una marca en esa posición :(\n")
    
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
datos_jugador = {"nombre":"", "marca_juego":"", "jugada":""}
datos_computadora = {"nombre":obtener_nombre_computadora(), "marca_juego":"", "jugada":""}
opcion_menu = ""
regresar_menu = ""
tablero = {}

# Juego como tal
while (opcion_menu != "s"):
    imprimir_menu()
    opcion_menu = input(("\nElige una opción: "))

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
        