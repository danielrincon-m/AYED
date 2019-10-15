from sys import stdin


def main():
    cases = int(stdin.readline().strip())
    for case in range(cases):
        nHouses = int(stdin.readline().strip())
        m1 = [0 for x in range(nHouses - 1)]
        m2 = [0 for x in range(nHouses - 1)]
        values = [int(x) for x in stdin.readline().strip().split()]

        for i in range(len(values) - 1):
            if i == 0:
                m1[0] = values[0]
            elif i == 1:
                m1[1] = max(m1[0], values[1])
            else:
                m1[i] = max(values[i] + m1[i - 2], m1[i - 1])

        for i in range(1, len(values)):
            if i == 1:
                m2[0] = values[1]
            elif i == 2:
                m2[1] = max(m2[0], values[2])
            else:
                m2[i - 1] = max(values[i] + m2[i - 3], m2[i - 2])
        answ = max(m1[nHouses - 2], m2[nHouses - 2])

        print('Caso #' + str(case + 1) + ': ' + str(answ))


main()
