from sys import stdin

sets = {}
adj = {}
consec = 0

def makeSet(node):
    global sets, adj, consec

    sets[consec] = {node}
    adj[node] = consec
    consec += 1

def findset(node):
    global sets, adj, consec

    return sets[adj[node]]

def joinSets(s1, s2):
    global sets, adj, consec

    newSet = s1.union(s2)
    sets[consec] = newSet
    for elt in s1:
        adj[elt] = consec
    for elt in s2:
        adj[elt] = consec
    consec += 1

def join(el1, el2):
    global sets, adj, consec

    s1 = findset(el1)
    s2 = findset(el2)
    if s1 != s2:
        joinSets(s1, s2)

def sameSet(el1, el2):
    global sets, adj, consec

    if sets[adj[el1]] == sets[adj[el2]]:
        return True
    return False


def main():
    global sets, adj, consec

    ncases = int(stdin.readline().strip())
    void = stdin.readline()
    for c in range(ncases):
        sets = {}
        adj = {}
        consec = 0

        aff = 0
        neg = 0
        nNodes = int(stdin.readline().strip())

        for i in range(nNodes):
            makeSet(str(i + 1))

        inp = stdin.readline().strip()
        while inp != '':
            comm, n1, n2 = inp.split()
            if comm == 'c':
                join(n1, n2)
            else:
                if sameSet(n1, n2):
                    aff += 1
                else:
                    neg += 1
            inp = stdin.readline().strip()
        print(str(aff) + ',' + str(neg))
        if c != ncases - 1:
            print()


main()

