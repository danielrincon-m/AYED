from sys import stdin


class Nodo:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def printPost(self):
        if self.left is not None:
            self.left.printPost()
        if self.right is not None:
            self.right.printPost()
        print(self.value, end='')


class Arbol:
    def __init__(self):
        self.raiz = None

    def buildTree(self, preord, inord, inBeg, inEnd, preIndex):
        if inBeg > inEnd:
            return None

        value = preord[preIndex]
        actualNode = Nodo(value)
        inIndex = inord.index(value)

        if inIndex < inBeg:
            return self.buildTree(preord, inord, inBeg, inEnd, preIndex + 1)
        if self.raiz is None:
            self.raiz = actualNode

        leftNode = self.buildTree(preord, inord, inBeg, inIndex - 1, preIndex + 1)
        rightNode = self.buildTree(preord, inord, inIndex + 1, inEnd, preIndex + 1)
        actualNode.setLeft(leftNode)
        actualNode.setRight(rightNode)

        return actualNode

    def printPos(self):
        if self.raiz is not None:
            self.raiz.printPost()
        print()


def main():
    entrada = stdin.readline().strip()
    while entrada != '':
        preord, inord = entrada.split()
        tree = Arbol()
        tree.buildTree(preord, inord, 0, len(inord) - 1, 0)
        tree.printPos()
        entrada = stdin.readline().strip()


main()
