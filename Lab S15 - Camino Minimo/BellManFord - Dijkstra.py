from sys import stdin
import math


class Node:
    def __init__(self, name):
        self.name = name
        self.d = math.inf
        self.phi = None

    def initialize(self):
        self.d = math.inf
        self.phi = None

    def getName(self):
        return self.name

    def setD(self, value):
        self.d = value

    def getD(self):
        return self.d

    def setPhi(self, value):
        self.phi = value

    def getPhi(self):
        return self.phi

    def getInfo(self):
        return (self.name, self.phi, self.d)


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def getWeight(self):
        return self.weight

    def getTripla(self):
        return (self.start, self.end, self.weight)


class Graph:
    #Los nodes son una lista de nombres de nodos
    #Los edges son una lista de triplas (inicio, fin, peso)
    def __init__(self, V, E):
        self.nodes = {}
        self.edges = []

        for node in V:
            self.nodes[node] = Node(node)
        for edge in E:
            self.edges.append(Edge(edge[0], edge[1], int(edge[2])))

    def addNode(self, name):
        self.nodes[name] = Node(name)

    def addEdge(self, edge):
        if edge[0] not in self.nodes:
            self.addNode(edge[0])
        if edge[1] not in self.nodes:
            self.addNode(edge[1])
        self.edges.append(Edge(edge[0], edge[1], int(edge[2])))

    def getNodes(self):
        return self.nodes.keys()

    def getEdges(self, getSorted = False):
        if not getSorted:
            return self.edges
        else:
            return sorted(self.edges, key=lambda edge: (edge.weight, edge.start, edge.end))

    def initializeSingleSource(self, source):
        for node in self.nodes:
            self.nodes[node].initialize()
        self.nodes[source].setD(0)

    def relax(self, edge):
        u = self.nodes[edge.getStart()]
        v = self.nodes[edge.getEnd()]
        w = edge.getWeight()
        if v.getD() > u.getD() + w:
            v.setD(u.getD() + w)
            v.setPhi(u.getName())
            return True
        return False

    def bellManFord(self, source):
        self.initializeSingleSource(source)
        for i in range(len(self.nodes)):
            for edge in self.edges:
                self.relax(edge)
        for edge in self.edges:
            if self.relax(edge):
                return False
        return True

    def dijkstra(self, source):
        self.initializeSingleSource(source)
        s = []
        q = list(self.nodes)
        while len(q) > 0:
            u = self.getMin(q)
            q.remove(u)
            s.append(u)
            adj = self.getNeighbors(u)
            for edge in adj:
                self.relax(edge)

    def getMin(self, q):
        m = min(q, key=lambda d: (self.nodes[d].getD()))
        return m

    def getNeighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if edge.getStart() == self.nodes[node].getName():
                neighbors.append(edge)
        return neighbors

    def printGraph(self):
        print()
        print('Nodes = '.join(self.getNodes()))
        print("Edges:")
        for edge in self.getEdges(True):
            print(edge.getTripla())
        print()

    def printResult(self):
        print()
        for node in self.nodes:
            print(self.nodes[node].getInfo())
        print()


def main():
    nodes = stdin.readline().strip().split()
    nEdges = int(stdin.readline().strip())
    edges = []
    for i in range(nEdges):
        edge = tuple(stdin.readline().strip().split())
        edges.append((edge[0], edge[1], int(edge[2])))

    graph = Graph(nodes, edges)
    #graph.bellManFord('A')
    graph.dijkstra('A')
    graph.printResult()



main()

'''
A B C D E F G
10
A B 7
A C 3
A E 2
B D 5
B C 10
C E 5
D E 8
D F 25
D G 45
F G 30
'''
'''
A B C D F G H I J
12
A B 15
A C 2
A D 20
C D 3
C J 13
D F 25
D G 5
D H 2
F G 35
G I 100
H I 1
I J 55
'''
