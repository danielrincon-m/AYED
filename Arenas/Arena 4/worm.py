#wormholes

from sys import stdin
import math

def bellManFord(source, nodes, edges):
    nodes[source] = (0, None)
    for i in range(len(nodes) - 1):
        changed = False
        for edge in edges:
            u = nodes[edge[0]]
            v = nodes[edge[1]]
            w = edge[2]
            if v[0] > u[0] + w:
                nodes[edge[1]] = (u[0] + w, edge[0])
                changed = True
        if not changed:
            return False
    for edge in edges:
        u = nodes[edge[0]]
        v = nodes[edge[1]]
        w = edge[2]
        if v[0] > u[0] + w:
            nodes[edge[1]] = (u[0] + w, edge[0])
            return True
    return False


def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        N = {}
        E = []
        n, m = stdin.readline().strip().split()
        for star in range(int(n)):
            N[str(star)] = (math.inf, None)
        for wh in range(int(m)):
            wormhole = stdin.readline().strip().split()
            E.append((wormhole[0], wormhole[1], int(wormhole[2])))
        print('possible' if bellManFord('0', N, E) is True else 'not possible')


main()
