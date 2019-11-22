class Node:
    def __init__(self, name):
        self.name = name

class edge:
    def __init__(self, node1, node2, weight):
        self.n1 = node1
        self.n2 = node2
        self.weight = weight

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def addEdge(self, u, v):


    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
            return visited

    def DFSUtil(self, v, visited):
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

        # The function to do DFS traversal. It uses
        # recursive DFSUtil()
    def DFS(self, v):
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        # DFS traversal
        self.DFSUtil(v, visited)
        return visited

    def MST_Prim(self):


def main():
    #Defimne
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)


    bfs = g.BFS(2)
    dfs = g.DFS(0)

    print('BFS:')
    print(2, ' :  ', end='')

    for el in range(len(bfs)):
        print(el, ',', end='')
    print()
    print('DFS:')
    print(2, ' :  ', end='')
    for el in range(len(dfs)):
        print(el, ',', end='')


main()