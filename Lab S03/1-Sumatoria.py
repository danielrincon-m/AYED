from sys import stdin


def sum(n):
    if n == 0:
        return n
    return n + sum(n - 1)


def main():
    n = int(stdin.readline().strip())
    print(sum(n))


main()
