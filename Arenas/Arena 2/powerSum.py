from sys import stdin
import math

OBJETIVO = math.inf
POTENCIA_OBJVO = math.inf
RAIZ_OBJVO = -1


# def powerSum(suma, valorASumar):
#     if suma == OBJETIVO:
#         return 1
#     elif suma > OBJETIVO or valorASumar > RAIZ_OBJVO:
#         return 0
#     return powerSum(suma + valorASumar ** POTENCIA_OBJVO, valorASumar + 1) + powerSum(suma, valorASumar + 1)


def memoPowerSum(suma, valorASumar, M):
    if (suma, valorASumar, OBJETIVO, POTENCIA_OBJVO) in M:
        return M[(suma, valorASumar, OBJETIVO, POTENCIA_OBJVO)]
    M[(suma, valorASumar, OBJETIVO, POTENCIA_OBJVO)] = powerSumP(suma, valorASumar, M)
    return M[(suma, valorASumar, OBJETIVO, POTENCIA_OBJVO)]


def powerSumP(suma, valorASumar, M):
    if suma == OBJETIVO:
        return 1
    elif suma > OBJETIVO or valorASumar > RAIZ_OBJVO:
        return 0
    return memoPowerSum(suma + valorASumar ** POTENCIA_OBJVO, valorASumar + 1, M) + memoPowerSum(suma, valorASumar + 1, M)


def main():
    global OBJETIVO, POTENCIA_OBJVO, RAIZ_OBJVO
    M = {}
    OBJETIVO = stdin.readline().strip()
    while OBJETIVO != '':
        OBJETIVO = int(OBJETIVO)
        POTENCIA_OBJVO = int(stdin.readline().strip())
        RAIZ_OBJVO = int(OBJETIVO**(1 / POTENCIA_OBJVO)) + 1
        casosExitosos = memoPowerSum(0, 1, M)
        # for key, value in M.items():
        #     print(key, value)
        print(casosExitosos)

        OBJETIVO = stdin.readline().strip()


main()
