from sys import stdin


def inv(s):
    if len(s) == 1:
        return s
    return [s[len(s) - 1]] + inv(s[:len(s) - 1])


def main():
    s = [int(x) for x in stdin.readline().strip().split(" ")]
    print(inv(s))


main()
