from sys import stdin

#Clase que representa un heap en una lsita
class Heap:

    #Función que inicializa las variables necesarias para la clase
    #Param: -policy: #True: max-heap; False: min-heap
    def __init__(self, policy):
        self.heap = []
        self.heap_size = None
        self.policy = policy

    # Función que calcula la posición del padre del elemento i
    # param: i: posición en la lista del elemento
    # Return : posición en la lista del padre del elemento i
    def parent(self, i):
        return i // 2

    # Función que calcula la posición del hijo izquierdo del elemento i
    # param: i: posición en la lista del elemento
    # Return : posición en la lista del hijo izquierdo del elemento i
    def left(self, i):
        return 2 * i

    # Función que calcula la posición del hijo derecho del elemento i
    # param: i: posición en la lista del elemento
    # Return : posición en la lista del hijo derecho del elemento i
    def right(self, i):
        return 2 * i + 1

    # Función que, según la política llama a max_heapify o min_heapify
    # param: i: Elemento para enviar a la función llamada
    def heapify (self, i):
        if self.policy is True:
            self.max_heapify(i)
        else:
            self.min_heapify(i)

    # Función que verifica si el elememto i es mayor a sus hijos, y si es menor lo intercambia con el hijo mayor
    # param: i: el elemento a comparar con sus dos hijos
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    # Función que verifica si el elememto i es menor a sus hijos, y si es mayor lo intercambia con el hijo menor
    # param: i: el elemento a comparar con sus dos hijos
    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.heap[l] < self.heap[i]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and self.heap[r] < self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    # Función que se encarga de aplicar heapify para cada elemento del heap
    # param: A: la lista que se desea convertir en heap
    def build_heap(self, A):
        self.heap = A
        self.heap_size = len(A) - 1
        for i in range(self.heap_size, -1, -1):
            self.heapify(i)

    # función que retorna la lista que representa al heap
    def getHeap(self):
        return self.heap

    # función que inserta el elemento 'el' a la lista y reconstruye el heap
    # param : el: elemento a insertar
    def insert(self, el):
        self.heap.append(el)
        self.build_heap(self.heap)

    # función que borra el elemento ubicado en el indice 'index' y reconstruye el heap
    # param : index: indice del elemento a eliminar
    def delete(self, index):
        self.build_heap(self.heap[:index]+self.heap[index+1:])

    # Función que actualiza el valor del elemento en la posición 'index' y reconstruye el heap
    # param: index: indice del elemento a actualizar
    #                newVal: valor nuevo del elemento en el indice 'index'
    def update(self, index, newVal):
        self.heap[index] = newVal
        self.build_heap(self.heap)


# función encargada de generar una lista a partir de una entrada
# return: lista de elementos
def entrada():
    return [int(x) for x in stdin.readline().strip().split()]


# función principal
def main():
    lista = entrada()

    heap = Heap(True)
    heap.build_heap(lista)
    print(heap.getHeap())

    heap = Heap(False)
    heap.build_heap(lista)
    print(heap.getHeap())


main()
