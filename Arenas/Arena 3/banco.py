from sys import stdin


class Node:
    def __init__(self, value, prev, next):
        self.prev = prev
        self.next = next
        self.value = value

    def setNext(self, node):
        self.next = node

    def getNext(self):
        return self.next

    def setPrev(self, node):
        self.prev = node

    def getPrev(self):
        return self.prev

    def getValue(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNodeBack(self, value):
        if self.head == None:
            node = Node(value, None, None)
            self.head = node
            self.tail = node
        else:
            node = Node(value, self.tail, None)
            self.tail.setNext(node)
            self.tail = node

    def removeNodeFront(self):
        if self.head == None:
            return None
        val = self.head.getValue()
        newHead = self.head.getNext()
        if newHead is not None:
            newHead.setPrev(None)
        self.head = newHead
        return val


def main():
    cases = int(stdin.readline().strip())
    for case in range(cases):
        bankQueue = LinkedList()
        instructions = int(stdin.readline().strip())
        for i in range(instructions):
            instruc = stdin.readline().strip()
            if instruc == 'Siguiente':
                next = bankQueue.removeNodeFront()
                if next == None:
                    print('No hay fila')
                else:
                    print(next)
            else:
                bankQueue.addNodeBack(instruc)


main()
