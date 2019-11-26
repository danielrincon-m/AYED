from sys import stdin


# Clase DisjointSet
class DisjointSet:
    def __init__(self):
        self.setList = {}
        self.pos = {}
        self.nextKey = 1

    def getKey(self):
        key = self.nextKey
        self.nextKey += 1
        return key

    def makeSet(self, rep):
        key = self.getKey()
        self.setList[key] = ({rep})
        self.pos[rep] = key

    def findSet(self, rep):
        if rep in self.pos:
            return self.setList[self.pos[rep]]
        return set()

    def union(self, st1, st2, r1, r2):
        key = self.getKey()

        del self.setList[self.pos[r1]]
        del self.setList[self.pos[r2]]

        newSet = st1.union(st2)
        self.setList[key] = newSet

        for elt in newSet:
            self.pos[elt] = key

    def getSetList(self):
        return self.setList

    def joinSets(self, r1, r2):
        set1 = self.findSet(r1)
        set2 = self.findSet(r2)
        if set1 != set2:
            self.union(set1, set2, r1, r2)

    def findConnectedRegions(self, graph):
        #Make Sets
        for v in graph['V']:
            self.makeSet(v)
        #For each relationship, Join Sets
        for arc in graph['E']:
            self.joinSets(arc[0], arc[1])
        return self.getSetList()


def main():
    cases = int(stdin.readline().strip())
    for c in range(cases):
        graph = {'V': [], 'E': []}
        n, m = map(int, stdin.readline().strip().split())
        graph['V'] = [str(i + 1) for i in range(n)]
        ds = DisjointSet()
        for couple in range(m):
            a, b = stdin.readline().strip().split()
            graph['E'].append((a, b))
        finalSets = ds.findConnectedRegions(graph)
        print(max([len(finalSets[i]) for i in finalSets.keys()]))


main()

'''
2
3 2
1 2
2 3
10 12
1 2
3 1
3 4
5 4
3 5
4 6
5 2
2 1
7 1
1 2
9 10
8 9

'''