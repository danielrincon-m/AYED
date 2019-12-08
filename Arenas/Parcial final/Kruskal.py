class Kruskal:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.sets = []
        for node in self.nodes:
            self.makeSet(node)
        self.edges = edges

    def makeSet(self, node):
        self.sets.append({node})

    def findset(self, node):
        for set in self.sets:
            if node in set:
                return set

    def joinSets(self, s1, s2):
        print(self.sets)
        newSet = s1.union(s2)
        self.sets.remove(s1)
        self.sets.remove(s2)
        self.sets.append(newSet)
        print(self.sets)

    def kruskal(self):
        tempEdges = sorted(self.edges, key=lambda d: d[2])
        print(tempEdges)
        minTree = []
        while len(tempEdges) > 0:
            minEdge = tempEdges.pop(0)
            s1 = self.findset(minEdge[0])
            s2 = self.findset(minEdge[1])
            if s1 != s2:
                minTree.append(minEdge)
                self.joinSets(s1, s2)
        return minTree

a = Kruskal(['a', 'b', 'c', 'd', 'e'], [('a', 'b', 3), ('a', 'd', 2), ('d', 'c', 5), ('b', 'c', 1), ('c', 'e', 3)])
print(a.kruskal())
