#SOLUCION AL PROBLEMA AGTC 3356, Simón Marín
from sys import stdin

#Función que se encarga de minimizar el número de operaciones posibles para transformar cualquier cadena c1 en una cadena c2.
#param -c1: cadena numero 1
#      -c2: cadena numero 2
#return -mínimo de operaciones posibles para transformar cadena c1 a cadena c2.
def cadenas(c1,c2):
    #Caso base, alguna cadena vacia
    if c1 == '' or c2 == '':
        return 0
    elif c1[0] == c2[0]:
        return cadenas(c1[1:],c2[1:])
    else:
        return min(1+cadenas(c1[1:],c2),1+cadenas(c1,c2[1:]),1+cadenas(c1[1:],c2[1:]))
#Función Principal.
def main():
    while True:
        try:
            long1,cadena1 = [x for x in stdin.readline().strip().split()]
            long2,cadena2 = [x for x in stdin.readline().strip().split()]
            print(cadenas(cadena1,cadena2))
        except ValueError:
            break
main()
#Función de pruebas, se realizan las correspondientes pruebas para verificar el funcionamiento del codigo
#return -Resultado de la prueba.
def pruebas():
    cadena1 = "AGTCTGACGC"
    cadena2 = "AGTAAGTAGGC"
    #Respuesta = 4, para pasar de cadena1 a cadena2 es necesario cambiar 3 letrasy eliminar una letra en la cadena2 
    respuesta = 4
    mi_respuesta = cadenas(cadena1,cadena2)
    if mi_respuesta == respuesta:
        return "Prueba pasada con exito."
    return "Prueba fallida."
