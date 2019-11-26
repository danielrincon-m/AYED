# Daniel Felipe Rincón Muñoz
from sys import stdin

# Clase DisjointSet
class DisjointSet:
    def __init__(self):
        self.setList = []

    def makeSet(self, rep):
        self.setList.append({rep})

    def findSet(self, rep):
        for st in self.setList:
            if rep in st:
                return st
        return set()

    def union(self, st1, st2):
        self.setList.remove(st1)
        if( st1 != st2 ):
          self.setList.remove(st2)
        self.setList.append(st1.union(st2))

    def getSetList(self):
        return self.setList

    def joinSets(self, r1, r2):
        self.union(self.findSet(r1), self.findSet(r2))

    def findConnectedRegions(self, graph):
        #Make Sets
        for v in graph['V']:
            self.makeSet(v)
        #For each relationship, Join Sets
        for arc in graph['E']:
            print('Before Join', arc, self.getSetList())
            self.joinSets(arc[0], arc[1])
            print('After Join', arc, self.getSetList())

        print(self.getSetList())

# Funcion que se encarga de encontrar el grafo de menor costo en donde todos los nodos estén conectados
def MST_Kruskal(graph):
    mst = {'V': graph['V'], 'E': []}
    ds = DisjointSet()
    graph['E'] = sorted(graph['E'], key=lambda arc: (arc[2], arc[0], arc[1]))
    for vertex in graph['V']:
        ds.makeSet(vertex)
    for edge in graph['E']:
        s1, s2 = ds.findSet(edge[0]), ds.findSet(edge[1])
        if s1 != s2:
            mst['E'].append(edge)
            ds.union(s1,s2)
    return mst

#Función principal
def main():
    graph = {'V': [], 'E': []}

    v = stdin.readline().strip().split()
    graph['V'] = v

    n = int(stdin.readline().strip())
    for i in range(n):
        e = stdin.readline().strip().split()
        edge = (e[0], e[1], int(e[2]))
        graph['E'].append(edge)
    mst = MST_Kruskal(graph)

    print(mst['V'])
    for e in mst['E']:
        print(e)

main()