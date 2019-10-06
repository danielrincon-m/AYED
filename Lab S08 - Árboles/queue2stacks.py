from sys import stdin


#clase de una cola realizada con una lista
class Queue:
    #Inicialización de la clase
    def __init__(self):
        self.queue = []

    #Función que se encarga de agregar un elemento a la cola
    #Param: -value: un elemento para agregar a la cola
    def put(self, value):
        self.queue.append(value)

    # Función que se encarga de quitarle un elemento a la cola
    def pop(self):
        del(self.queue[0])

    # Función que se encarga de retornar el primer elemento de la cola
    # Return: El primer elemento de la cola
    def peek(self):
        return self.queue[0]


# Función principal
def main():
    cola = Queue()
    queries = int(stdin.readline().strip())
    tipo = None
    x = None
    for i in range(queries):
        query = stdin.readline().strip()
        if query[0] == '1':
            tipo, x = [int(x) for x in query.split()]
            cola.put(x)
        else:
            tipo = int(query[0])
            if tipo == 2:
                cola.pop()
            else:
                print(cola.peek())


main()