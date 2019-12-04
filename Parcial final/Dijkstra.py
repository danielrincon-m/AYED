import math

class Dijkstra:
    def __init__(self, nodes, edges):
        self.nodes = {}
        for node in nodes:
            self.nodes[node] = [math.inf, None]
        self.edges = edges

    def relax(self, edge):
        if edge[1].d > edge[0].d + edge[2]:
            edge[1].d = edge[0].d + edge[2]
            edge[1].pi = edge[0]
            return True
        return False

    def init(self, source):
        for node in self.nodes:
            node = [math.inf, None]
        self.nodes[source] = [0, None]

    def neigbours(self, node):
        neigh = []
        for edge in self.edges:
            if edge[0] == node:
                neigh.append(edge)

        return neigh

    def dijkstra(self, source):
        self.init(source)
        tempNodes = []
        tempNodes.append((source, self.nodes[source][0]))
        while tempNodes:
            tempNodes = sorted(tempNodes, key=lambda d: d[1])
            minNode = tempNodes.pop(0)[0]
            neigh = self.neigbours(minNode)
            for edge in neigh:
                ans =self.relax(edge)
                if ans:
                    tempNodes.append(edge[1])
        return