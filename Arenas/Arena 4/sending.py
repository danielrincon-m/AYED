#sending email

from sys import stdin
import math
import heapq


class Graph:
    def __init__(self):
        self.nodes = {} # {name: (d, phi)}
        self.edges = [] # [(start, end, weight)]
        self.neighbors = {} # {startName: [edgesIndex]}
        self.visited = {}

    def createGraph(self, V, E):
        for node in V:
            self.nodes[node] = (math.inf, None)
            self.visited[node] = False
        for edge in E:
            self.edges.append((edge[0], edge[1], int(edge[2])))
            if edge[0] not in self.neighbors:
                self.neighbors[edge[0]] = []
            self.neighbors[edge[0]].append(len(self.edges) - 1)

    def clearGraph(self):
        self.nodes.clear()
        self.edges.clear()
        self.neighbors.clear()
        self.visited.clear()

    def getNodeD(self, name):
        return self.nodes[name][0]

    def initializeSingleSource(self, source):
        for node in self.nodes:
            self.nodes[node] = (math.inf, None)
        self.nodes[source] = (0, None)
        for node in self.visited:
            self.visited[node] = False

    def relax(self, edge):
        u = self.nodes[edge[0]]
        v = self.nodes[edge[1]]
        w = edge[2]
        if v[0] > u[0] + w:
            self.nodes[edge[1]] = (u[0] + w, edge[0])
            return True
        return False

    def dijkstra(self, source):
        self.initializeSingleSource(source)
        q = []
        heapq.heappush(q, (0, source))
        while q:
            #print(q)
            u = heapq.heappop(q)
            self.visited[u[1]] = True
            adj = self.getNeighbors(u[1])
            for edge in adj:
                #if not self.visited[edge[1]]:
                result = self.relax(edge)
                if result:
                    heapq.heappush(q, (edge[2], edge[1]))

    def getNeighbors(self, node):
        neigh = []
        if node in self.neighbors:
            for edge in self.neighbors[node]:
                neigh.append(self.edges[edge])
        return neigh

#import time
def main():
    #totalTime = 0
    cases = int(stdin.readline().strip())
    g = Graph()
    for c in range(cases):
        g.clearGraph()
        n, m, s, t = stdin.readline().strip().split()
        nodes = [str(i) for i in range(int(n))]
        edges = []
        for conn in range(int(m)):
            inp = stdin.readline().strip().split()
            edges.append((inp[0], inp[1], int(inp[2])))
            edges.append((inp[1], inp[0], int(inp[2])))

        g.createGraph(nodes, edges)
        #ti = time.time()
        g.dijkstra(s)
        #totalTime += (time.time() - ti)
        ans = g.getNodeD(t)
        pans = str(ans) if ans != math.inf else "unreachable"
        print("Case #" + str(c + 1) + ": " + pans)
    #print("total dijkstra time: ", time.time() - ti)


main()

'''
3
2 1 0 1
0 1 100
3 3 2 0
0 1 100
0 2 200
1 2 50
2 0 0 1
'''