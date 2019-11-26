from sys import stdin


def main():
    cases = int(stdin.readline().strip())
    stdin.readline() #first white line
    for i in range(cases):
        if i != 0:
            print()

        trees = {}
        tree = stdin.readline().strip()
        total = 0

        while tree != '':
            if tree not in trees:
                trees[tree] = 1
            else:
                trees[tree] += 1
            total += 1
            tree = stdin.readline().strip()

        ltrees = [(d, trees[d]) for d in trees]
        ltrees = sorted(ltrees, key= lambda d: (d[0]))

        for elt in ltrees:
            print(elt[0], "{0:.4f}".format(elt[1] * 100 / total))


main()
