#Solución del problema pila o cola - Daniel Rincón
from sys import stdin
import queue


#Función que se encarga de iterar sobre la salida y verificar que los valores de pila y cola correspondan
#Param: -pila: la pila construida con la entrada
#       -cola: la cola construida con la entrada
#       -salida: la salida que entrega el problema
#Return: 'pila' si la salida corresponde a una pila, 'cola' si corresponde a una cola, y 'ambas'
def analize(pila, cola, salida):
    esPila = True
    esCola = True
    for item in salida:
        if pila.get() != item:
            esPila = False
        if cola.get() != item:
            esCola = False
    if esPila and esCola:
        return 'ambas'
    elif esPila:
        return 'pila'
    elif esCola:
        return 'cola'
    else:
        return 'ninguna'


#Función que se encarga de construir una pila y una cola con la entrada
#Param: -entrada: una lista de enteros que corresponden a la entrada
#Return: la pila y la cola construidas
def buildDataStructures(entrada):
    pila = queue.LifoQueue()
    cola = queue.Queue()
    for item in entrada:
        pila.put(item)
        cola.put(item)
    return pila, cola


#Función principal
def main():
    n = stdin.readline().strip()
    while n != '':
        entrada = [int(x) for x in stdin.readline().strip().split()]
        salida = [int(x) for x in stdin.readline().strip().split()]
        pila, cola = buildDataStructures(entrada)
        print(analize(pila, cola, salida))
        n = stdin.readline().strip()


main()
