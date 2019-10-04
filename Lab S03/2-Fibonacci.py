from sys import stdin


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    n = int(stdin.readline().strip())
    print(fibonacci(n))


main()
