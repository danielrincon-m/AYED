from sys import stdin
import sys


def uqs(seq):
    if len(seq) <= 1:
        return 0
    min_pos = seq.index(min(seq))
    del(seq[min_pos])
    return min_pos + uqs(seq)


def main():
    sys.setrecursionlimit(100000)
    n = int(stdin.readline().strip())
    while n != 0:
        seq = []
        for i in range(n):
            seq.append(int(stdin.readline().strip()))
        print(uqs(seq))
        n = int(stdin.readline().strip())


main()
