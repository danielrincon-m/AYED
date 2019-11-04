from sys import stdin

class Node:
    def __init__(self, name):
        self.name = name
        self.color = None

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def colored(self):
        if self.color is None:
            return False
        return True


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.isBicolor = True

    def addNode(self, name):
        self.nodes[name] = Node(name)
        self.edges[name] = []

    def addEdge(self, a, b):
        self.edges[a].append(b)

    def getGraph(self):
        return self.edges

    def getOtherColor(self, color):
        if color == 'red':
            return 'blue'
        else:
            return 'red'

    def bicolor(self):
        self.DFS()
        return self.isBicolor

    def DFS(self):
        for elt in self.nodes.keys():
            if not self.nodes[elt].colored():
                self.DFSVisit(elt, 'red')

    def DFSVisit(self, elt, color):
        if not self.nodes[elt].colored():
            self.nodes[elt].setColor(color)
        else:
            color = self.nodes[elt].getColor()

        for hijo in self.edges[elt]:
            if self.nodes[hijo].colored():
                if self.nodes[hijo].getColor() == color:
                    self.isBicolor = False
            else:
                self.DFSVisit(hijo, self.getOtherColor(color))


def main():
    nodes = int(stdin.readline().strip())
    while nodes != 0:
        graph = Graph()
        for i in range(nodes):
            graph.addNode(i)

        edges = int(stdin.readline().strip())
        for i in range(edges):
            a, b = [int(x) for x in stdin.readline().strip().split()]
            graph.addEdge(a, b)
            graph.addEdge(b, a)

        ans = graph.bicolor()
        #print(graph.getGraph())
        if ans == True:
            print('BICOLORABLE.')
        else:
            print('NOT BICOLORABLE.')

        nodes = int(stdin.readline().strip())


main()
