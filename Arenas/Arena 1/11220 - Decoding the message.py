# Algoritmo:
# 1. Leer la entrada, una lista de oraciones en donde cada oración es una lista de palabras.
# 2. Para cada lista de oraciones, definir una variable para la posición de letra, una lista de palabras de salida y una variable para la palabra de salida, recorrer la lista.
#      2.1. Verificar si la posición de la letra se encuentra en la palabra.
#      2.2. Si es así, agregar la letra a la palabra destino, agregar 1 a la posición de letra.
#      2.3. agregar la palabra final a la lista de salida.
# 3. Imprimir cada elemento de la lista de salida.

from sys import stdin


def leerEntrada():
    oraciones = []
    while True:
        oracion = stdin.readline().strip().split(" ")
        if oracion == [""]:
            break
        else:
            oraciones.append(oracion)
    return oraciones


def obtenerLetra(oracion, indiceDeLetra):
    return oracion[indiceDeLetra]


def construirSalida(oraciones):
    respuestas = []
    for i in range(len(oraciones)):
        indiceDeLetra = 0
        palabraConstruida = ""
        for j in range(len(oraciones[i])):
            if indiceDeLetra < len(oraciones[i][j]):
                palabraConstruida += obtenerLetra(oraciones[i][j], indiceDeLetra)
                indiceDeLetra += 1
        respuestas.append(palabraConstruida)
    return respuestas


def imprimirSalida(caso, respuestas):
    if caso != 1:
        print()
    print('Case #' + str(caso) + ":")
    for respuesta in respuestas:
        print(respuesta)


def main():
    casos = int(stdin.readline().strip())
    stdin.readline()

    for i in range(casos):
        oraciones = leerEntrada()
        respuestas = construirSalida(oraciones)
        imprimirSalida(i + 1, respuestas)


main()
