import math
import queue
from sys import stdin

class Grafo:
    def __init__(self, v, e):
        self.v = []
        self.e = {}
        #Mapear relaciones desde los arcos
        for arco in e:
            self.addEdge(arco)

    def initializeEdge(self, value):
        return {'value': value, 'color': None, 'dist': None, 'phi': None }

        
    def addEdge(self, e):
        nodo1,nodo2 = e[0],e[1]
        if nodo1 in self.e.keys():
            self.e[nodo1].append(nodo2)
        else:
            self.e[nodo1] = [nodo2]

        existsN1 = False
        existsN2 = False

        for vertex in self.v:
            existsN1 = existsN1 or (vertex['value'] == nodo1)
            existsN2 = existsN2 or (vertex['value'] == nodo2)

        if not existsN1:
            self.v.append(self.initializeEdge(nodo1))
            
        if not existsN2:
            self.v.append(self.initializeEdge(nodo2))
             

    def getNeighbors(self, value):
        neighbors = self.e[value] if value in self.e.keys() else []
        retArray = []
        for e in neighbors:
            #Buscar los atributos de ese vertice
            for u in self.v:
                if u['value'] == e:
                    retArray.append(u)

        return retArray

    def BFS(self, s):
        processQueue = queue.Queue()
        for u in self.v :
            value = u['value']
            if value != s:
                u['color'] = 'WHITE'
                u['dist'] = math.inf
                u['phi'] = None
            else:
                u['color'] = 'GRAY'
                u['dist'] = 0
                u['phi'] = None
                processQueue.put(u)

        while not processQueue.empty():
            u = processQueue.get()
            neigh = self.getNeighbors(u['value'])

            for vec in neigh:
                if vec['color'] == 'WHITE':
                    vec['color'] = 'GRAY'
                    vec['dist'] = u['dist'] + 1
                    vec['phi'] = u
                    processQueue.put(vec)
            u['color']='Black'
        return self.v

    def DFS(self):
        for u in self.v:
            u['color'] = 'WHITE'
            u['phi'] = None
        time = 0
        for u in self.v:
            if u['color'] == 'WHITE':
                self.DFS_visit(u, time)
        return self.v

    def DFS_visit(self, u, time):
        u['dist'] = time
        time += 1
        u['color'] = 'GRAY'
        neigh = self.getNeighbors(u['value'])

        for vec in neigh:
            if vec['color'] == 'WHITE':
                vec['phi'] = u
                self.DFS_visit(vec, time)
        u['color'] = 'BLACK'

def main():
    vertex = stdin.readline().strip().split()
    arcsSize = int(stdin.readline().strip())
    arcs = []
    for i in range(arcsSize):
        inp = stdin.readline().strip().split()
        arcs.append((inp[0], inp[1]))

    # grafo = Grafo(vertex, arcs)
    # s = stdin.readline().strip()
    # vertex = grafo.BFS(s)

    grafo = Grafo(vertex, arcs)
    vertex = grafo.DFS()

    for u in vertex :
        antecesor = u['phi']
        if antecesor is None:
            print('Nodo %s tiene distancia %s desde %s ' % (u['value'], u['dist'], vertex[0]['value']) )
        else:
            print('Nodo %s tiene distancia %s desde %s con antecesor %s' % (u['value'], u['dist'], vertex[0]['value'], u['phi']['value'] ) )


main()