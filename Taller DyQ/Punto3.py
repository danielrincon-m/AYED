
def exp(a, n):
    if n == 1:
        return a
    elif n == 2:
        return a*a

    if n % 2 == 0:
        return exp(a, n//2) * exp(a, n//2)
    else:
        return exp(a, n // 2) * exp(a, n // 2 + 1)


def main():
    a = int(input('Numero base: '))
    n = int(input('Exponente: '))
    print(exp(a, n))

main()