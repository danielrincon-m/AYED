from sys import stdin
import sys
sys.setrecursionlimit(1000000000)
values = [1, 5, 10, 25, 50]


# def ways(n, actualIndex):
#     if n < 0 or actualIndex >= len(values):
#         return 0
#     elif n == 0:
#         return 1
#     return ways(n - values[actualIndex], actualIndex) + ways(n, actualIndex + 1)


def memoWays(n, actualIndex, M):
    if n < 0 or actualIndex >= len(values):
        return 0
    if (n, actualIndex) in M:
        return M[(n, actualIndex)]
    M[(n, actualIndex)] = waysP(n, actualIndex, M)
    return M[(n, actualIndex)]


def waysP(n, actualIndex, M):
    if n < 0 or actualIndex >= len(values):
        return 0
    elif n == 0:
        return 1
    return memoWays(n - values[actualIndex], actualIndex, M) + memoWays(n, actualIndex + 1, M)


def main():
    M = [[None for x in range(5)] for y in range(6)]
    M = {}
    inp = stdin.readline().strip()
    while inp != '':
        n = int(inp)
        #buenas = ways(n, 0)
        buenas = memoWays(n, 0, M)
        # for key, value in M.items():
        #     print(key, value)
        if buenas != 1:
            print('There are', str(buenas), 'ways to produce', str(n), 'cents change.')
        else:
            print('There is only', str(buenas), 'way to produce', str(n), 'cents change.')
        inp = stdin.readline().strip()


main()
