
def minimo(lista):
    n = len(lista)
    if n == 1:
        return lista[0]
    elif n == 2:
        return min(lista[0], lista[1])
    return min(minimo(lista[0:n//2]), minimo(lista[n//2:n]))


def main():
    n = int(input('Numero de elementos: '))
    lista = []
    for i in range(n):
        lista.append(int(input('Escriba un elemento: ')))
    print(minimo(lista))


main()
