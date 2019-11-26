#wormholes

from sys import stdin
import math


def initializeSingleSource(nodes, source):
    nodes[source] = (0, None)
    return nodes


def relax(nodes, edge):
    u = nodes[edge[0]]
    v = nodes[edge[1]]
    w = edge[2]
    if v[0] > u[0] + w:
        nodes[edge[1]] = (u[0] + w, edge[0])
        return nodes, True
    return nodes, False


def bellManFord(source, nodes, edges):
    nodes = initializeSingleSource(nodes, source)
    for i in range(len(nodes)):
        for edge in edges:
            nodes, a = relax(nodes, edge)
    for edge in edges:
        nodes, res = relax(nodes, edge)
        if res:
            return False
    return True


def main():
    cases = int(stdin.readline().strip())
    N = {}
    E = []
    for i in range(cases):
        N.clear()
        E.clear()
        n, m = stdin.readline().strip().split()
        for star in range(int(n)):
            N[str(star)] = (math.inf, None)
        for wh in range(int(m)):
            wormhole = stdin.readline().strip().split()
            E.append((wormhole[0], wormhole[1], int(wormhole[2])))
        print('possible' if bellManFord('0', N, E) is False else 'not possible')


main()
