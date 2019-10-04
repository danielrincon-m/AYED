from sys import stdin
import math

def tn1(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return 1 + tn1(n//2)
    return 1 + tn1(3 * n + 1)


def memotn1(n, M):
    if n in M:
        return M[n]
    M[n] = tn1p(n, M)
    return M[n]


def tn1p(n, M):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + memotn1(n//2, M)
    return 1 + memotn1(3 * n + 1, M)


def r3n1(a, b, M):
    maxLocal = -math.inf
    for i in range(a, b + 1):
        maxLocal = max(maxLocal, memotn1(i, M))
    return maxLocal


def main():
    entrada = [x for x in stdin.readline().strip().split(" ")]
    M = {}
    while entrada != [""]:
        a, b = int(entrada[0]), int(entrada[1])
        print(a, b, r3n1(min(a, b), max(a, b), M))
        entrada = [x for x in stdin.readline().strip().split(" ")]


main()
