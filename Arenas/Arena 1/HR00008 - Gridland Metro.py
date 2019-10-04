# Algoritmo:
# 1.Leer la entrada, variables separadas para tamaño y cantidad de lineas de metro
# 2.Generar una matriz del tamaño adecuado, inicializada en cero
# 3.Por cada una de las lineas de metro, ubicar un 1 en la fila y columnas indicadas
# 4.Contar el numero de celdas con 0 en la matriz
# 5.Divulgar respuesta

from sys import stdin


def leerEntrada():
    lineas = []
    datosIniciales = [int(x) for x in stdin.readline().strip().split(" ")]
    filas, cols, cantDeLineas = datosIniciales[0], datosIniciales[1], datosIniciales[2]
    for i in range(cantDeLineas):
        lineas.append([int(x) for x in stdin.readline().strip().split(" ")])
    return filas, cols, lineas


def crearMatrizRespuesta(filas, cols, lineas):
    matrizRespuesta = [[0 for i in range(cols)] for j in range(filas)]
    for i in range(len(lineas)):
        for j in range(lineas[i][1] - 1, lineas[i][2]):
            matrizRespuesta[lineas[i][0] - 1][j] = 1
    return matrizRespuesta


def calcularPostes(filas, cols, matrizRespuesta):
    numeroDePostes = 0
    for i in range(filas):
        for j in range(cols):
            if matrizRespuesta[i][j] == 0:
                numeroDePostes += 1
    return numeroDePostes


def main():
    filas, cols, lineas = leerEntrada()
    matrizRespuesta = crearMatrizRespuesta(filas, cols, lineas)
    numeroDePostes = calcularPostes(filas, cols, matrizRespuesta)
    print(numeroDePostes)


main()
