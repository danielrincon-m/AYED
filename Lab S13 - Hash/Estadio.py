from sys import stdin
import math
import random

class HashTable:
    def __init__(self, m):
        self.data = [ [] for i in range(m) ]
        self.A = 0.98

    def buildHash(self, v):
        for e in v:
            self.insert(e)
        
    def fHash(self, u):
        c=u
        return int(c[0])%4
        #return hash(u) % len(self.data)

    def insert(self, u):
        self.data[self.fHash(u)].append(u)

    def delete(self, u):
        self.data[self.fHash(u)].remove(u)

    def update(self, u1, u2):
        self.delete(u1)
        self.insert(u2)

    def search(self, u):
        slot = self.data[self.fHash(u)]
        for e in slot:
            if e == u:
                return e
        return None

    def getData(self):
        return self.data


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
    dato=input()
    print("Digite los datos de la siguiente forma y separados por un espacio: Tribuna-Cedula-Nombre-Cantidad  y presione la tecla Enter 2 veces.")
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
main()
