# Algoritmo:
# 1. Obtener matriz de numeros de la entrada
# 2. Realizar una lista de longitud (numero de filas de la matriz) en donde cada elemento
#    es la posición máxima en la que se podría mover una caja vacía (columna)
# 3. Recorrer la matriz desde la posición máxima de columna de cada fila hasta cero
#   3.1. Si se encuentra una caja moverla a la posición máxima y restarle 1
# 4. Imprimir la solución


from sys import stdin


def leerEntrada():
    size = [int(x) for x in stdin.readline().strip().split(" ")]
    filas, columnas = size[0], size[1]
    matrizEntrada = []
    for i in range(filas):
        matrizEntrada.append([int(x) for x in stdin.readline().strip().split(" ")])
    return filas, columnas, matrizEntrada


def computarPosiciones(filas, cols, matrizEntrada):
    posicionesMaximas = []
    for i in range(filas):
        posicionesMaximas.append(-1)
        for j in range(cols):
            if matrizEntrada[i][j] == 0:
                posicionesMaximas[i] = j
            elif matrizEntrada[i][j] == 2:
                break
    return posicionesMaximas


def calcularSolucion(filas, matrizEntrada, posicionesMaximas):
    for i in range(filas):
        for j in range(posicionesMaximas[i], -1, -1):
            if matrizEntrada[i][j] == 1:
                matrizEntrada[i][posicionesMaximas[i]] = 1
                posicionesMaximas[i] -= 1
                matrizEntrada[i][j] = 0
    return matrizEntrada


def imprimirRespuesta(filas, cols, matrizSolucion):
    for i in range(filas):
        for j in range(cols):
            print(matrizSolucion[i][j], end=' ')
        print()


def main():
    filas, columnas, matrizEntrada = leerEntrada()
    posicionesMaximas = computarPosiciones(filas, columnas, matrizEntrada)
    matrizSolucion = calcularSolucion(filas, matrizEntrada, posicionesMaximas)
    imprimirRespuesta(filas, columnas, matrizSolucion)


main()
