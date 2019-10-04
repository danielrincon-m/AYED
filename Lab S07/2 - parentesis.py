#SOLUCION AL PROBLEMA DE EMPAREJAMIENTO DE PARÉNTESIS - Daniel Rincón
from sys import stdin
import queue


#Función que se encarga de intentar colocar todos los parentesis de apertura en una pila, e intentar sacarlos cuando su correspondiente de cierre aparece
#Param: -secuencia: cadena de parentesis
#       -pila:pila que se utilizará para operar
#       -parejas: diccionario que contiene las parejas válidas
#Return: True si la cadena es válida, False si la cadena está incompleta, el índice en donde falla si la cadena es incorrecta
def analizar(secuencia, pila, parejas):
    for i in range(len(secuencia)):
        llave = secuencia[i]
        if llave in parejas:
            if pila.empty():
                return i
            top = pila.get()
            if top != parejas[llave]:
                return i
        else:
            pila.put(llave)
    if pila.empty():
        return True
    return False


#Función principal
def main():
    secuencia = stdin.readline().strip()
    pila = queue.LifoQueue()
    parejas = {")":"(",
               "}":"{",
               "]":"["}
    result = analizar(secuencia, pila, parejas)
    if result == True:
        print(True)
    elif result == False:
        print('Incomplete parenthesis (no se cerraron todos los abiertos)')
    else:
        print('Failed at:', result)


main()


#función para validar los posibles casos
def pruebas():
    #Se usan los 3 casos de prueba de los que se pueden obtener las 3 posibles respuestas de la función
    inputs = ['{}[](){{}}', '{{{{]}))', '{{[[]]}']
    results = [True, 4, False]
    pila = queue.LifoQueue()
    parejas = {")": "(",
               "}": "{",
               "]": "["}
    for i in range(len(inputs)):
        if analizar(inputs[i], pila, parejas) == results[i]:
            print('Caso correcto')
        else:
            print('Caso erroneo')


#pruebas()