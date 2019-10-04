from sys import stdin
import time


def superDigit(n):
    if len(n) == 1:
        return int(n)
    newDigit = 0
    for i in range(len(n)):
        newDigit += int(n[i])
    return superDigit(str(newDigit))


def memoSuperDigit(n, M):
    if n in M:
        return M[n]
    M[n] = superDigitP(n, M)
    return memoSuperDigit(n, M)


def superDigitP(n, M):
    if len(n) == 1:
        return int(n)
    newDigit = 0
    for i in range(len(n)):
        newDigit += int(n[i])
    return memoSuperDigit(str(newDigit), M)


def calcNumber(n, k):
    k = int(k)
    nb = n
    for i in range(0, k - 1):
        n += nb
    return(n)


def main():
    inp = [x for x in stdin.readline().strip().split(" ")]
    M = {}
    while inp != ['']:
        n, k = inp[0], inp[1]
        n = calcNumber(n, k)
        print(memoSuperDigit(n, M))

        inp = [x for x in stdin.readline().strip().split(" ")]


main()
