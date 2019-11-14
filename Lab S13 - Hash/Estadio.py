from sys import stdin

# Clase que respresenta una has table en una lista
class HashTable:

    # Función que inicializa las variables necesarias para la clase
    # Param: -m: Tamaño de la hash table
    def __init__(self, m):
        self.data = [ [] for i in range(m) ]
        self.A = 0.98

    # Función que pobla la hash table a partir de una lista de elementos
    # Param: -v: lista de elementos para añadir a la hash table
    def buildHash(self, v):
        for e in v:
            self.insert(e)

    # Función que calcula el hash correspondiente al elemento u
    # Param: -u: Elemento al cual se le calculará el hash
    # return: El hash calculado del elemento
    def fHash(self, u):
        c=u
        return int(c[0])%4
        #return hash(u) % len(self.data)

    # Función que inserta un elemento en la hash table, previamente calculado el hash
    # Param: -u: Elemento que se desea insertar a la hash table
    def insert(self, u):
        self.data[self.fHash(u)].append(u)

    # Función que elimina un elemento en la hash table, previamente calculado el hash
    # Param: -u: Elemento que se desea eliminar de la hash table
    def delete(self, u):
        self.data[self.fHash(u)].remove(u)

    # Función que actualiza un elemento en la hash table, previamente calculado el hash
    # Param: -u1: Elemento que se desea actualizar en la hash table
    #        -u2: Elemento por el cual se desea reemplazar u1
    def update(self, u1, u2):
        self.delete(u1)
        self.insert(u2)

    # Función que busca un elemento en la hash table, previamente calculado el hash
    # Param: -u: Elemento que se desea buscar en la hash table
    #return: El elemento buscado si existe en la hash table, o none si este no existe
    def search(self, u):
        slot = self.data[self.fHash(u)]
        for e in slot:
            if e == u:
                return e
        return None

    # Función que retorna los datos presentes en la hash table
    # Return: -Una lista con todos los elementos de la hash table
    def getData(self):
        return self.data

# Función principal
def main():
    hTable = HashTable(4)
    print("*************************************************")
    print("*******************BIENVENIDO********************")
    print("*************************************************")
    print("Digite solo el numero de la tribuna que desea comprar: ")
    print("1. Occidental")
    print("2. Oriental")
    print("3. Norte")
    print("4. Sur")
    #dato=input()
    print("Digite los datos de la siguiente forma y separados por un espacio: Tribuna Cedula Nombre Cantidad  y presione la tecla Enter 2 veces.")
    datos=stdin.readline().strip().split()
    while datos!=[]:
        if datos[0]=="1":
            total=int(datos[3])*50000
            print("Total: $",total)
        if datos[0]=="2":
            total=int(datos[3])*100000
            print("Total: $",total)
        if datos[0]=="3":
            total=int(datos[3])*30000
            print("Total: $",total)
        if datos[0]=="4":
            total=int(datos[3])*30000
            print("Total: $",total)
        hTable.buildHash([datos])
        datos=stdin.readline().strip().split()
    data = hTable.getData()
    print('Sur:', data[0])
    print('Occidental:', data[1])
    print('Oriental:', data[2])
    print('Norte:', data[3])

# Funcion de pruebas
def pruebas():
    hTable = HashTable(4)
    datos = [[1, 123456, 'Daniel', 5], [2, 548479458, 'Alejandro', 8], [3, 841321654, 'Jonathan', 9]]
    hTable.buildHash(datos)
    print(hTable.getData())

main()
#pruebas()
