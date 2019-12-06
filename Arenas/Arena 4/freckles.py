from sys import stdin
import math


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
            return True
        return False


# Funcion que se encarga de encontrar el grafo de menor costo en donde todos los nodos estén conectados
def MST_Kruskal(graph):
    mst = {'V': graph['V'], 'E': []}
    ds = DisjointSet()
    graph['E'] = sorted(graph['E'], key=lambda arc: (arc[2]))
    for vertex in graph['V']:
        ds.makeSet(vertex)
    for edge in graph['E']:
        res = ds.joinSets(edge[0], edge[1])
        if res:
            mst['E'].append(edge)
    return mst


def distsq(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2


def main():
    ncases = int(stdin.readline().strip())
    for n in range(ncases):
        if n != 0:
            print()
        blank = stdin.readline()
        graph = {'V': {}, 'E': []}
        npecas = int(stdin.readline().strip())
        for i in range(npecas):
            graph['V'][str(i)] = [float(x) for x in stdin.readline().strip().split()]
        for i in range(npecas):
            for j in range(i + 1, npecas):
                if i != j:
                    d = distsq(graph['V'][str(i)][0], graph['V'][str(i)][1], graph['V'][str(j)][0],graph['V'][str(j)][1])
                    graph['E'].append((str(i), str(j), d))
        mst = MST_Kruskal(graph)
        distanciasq = 0
        for edge in mst['E']:
            distanciasq += math.sqrt(edge[2])
        print('%.2f'%distanciasq)


main()
