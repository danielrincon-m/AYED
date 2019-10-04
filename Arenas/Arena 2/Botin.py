from sys import stdin
import math


def max_value(valores, valorActual, pesos, pesoActual, pesoMax, indiceActual):
    pesoActual += pesos[indiceActual]
    valorActual += valores[indiceActual]
    if pesoActual > pesoMax:
        return 0
    maxValor = -math.inf
    for i in range(indiceActual + 1, len(pesos)):
        valorResultado = max(valorActual, max_value(valores, valorActual, pesos, pesoActual, pesoMax, i))
        if valorResultado > maxValor:
            maxValor = valorResultado
    return maxValor


def main():
    casos = int(stdin.readline().strip())
    for i in range(casos):
        n, w = [int(x) for x in stdin.readline().strip().split(" ")]
        valores = [int(x) for x in stdin.readline().strip().split(" ")]
        pesos = [int(x) for x in stdin.readline().strip().split(" ")]
        max = -math.inf
        for j in range(len(pesos)):
            valorResultado = max_value(valores, 0, pesos, 0, w, j)
            if valorResultado > max:
                max = valorResultado
        print(max)


main()
