def main():
    n = int(input('Numero de elementos: '))
    lista = []
    for i in range(n):
        lista.append(int(input('Escriba un elemento: ')))
    for i in range(n - 1):
        if lista[i + 1] != lista[i] + 1:
            print('missing=' + str(lista[i] + 1))
            break


main()