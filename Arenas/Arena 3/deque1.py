from sys import stdin


class Node:
    def __init__(self, value, prev):
        self.prev = prev
        self.value = value

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

    def addNodeBottom(self, value):
        if self.tail == None:
            node = Node(value, None)
            self.head = node
            self.tail = node
        else:
            node = Node(value, None)
            self.head.setPrev(node)
            self.head = node

    def removeNodeTop(self):
        if self.tail == None:
            return None
        val = self.tail.getValue()
        newTail = self.tail.getPrev()
        if newTail is not None:
            self.tail = newTail
        else:
            self.tail = None
            self.head = None
        return val

    def isEmpty(self):
        return self.head == None

    def oneElement(self):
        return self.head == self.tail


# import time
def main():
    # startTime = time.time()
    # input = open('input.txt', 'r')
    # output = open('output.txt', 'w')
    n = int(stdin.readline().strip())
    # n = int(input.readline().strip())
    while n != 0:
        deck = LinkedList()
        discarded = []
        for i in range(1, n + 1):
            deck.addNodeBottom(i)
        while not deck.oneElement():
            discarded.append(deck.removeNodeTop())
            savedCard = deck.removeNodeTop()
            deck.addNodeBottom(savedCard)
        discarded.append(deck.removeNodeTop())

        print('Discarded cards: ', end='')
        for i in range(len(discarded) - 2):
            print(str(discarded[i]) + ', ', end='')
        print( str(discarded[len(discarded) - 2]))
        print('Remaining card: ' + str(discarded[len(discarded) - 1]))

        # output.write('Discarded cards: ')
        # for i in range(len(discarded) - 2):
        #     output.write(str(discarded[i]) + ', ')
        # output.write(str(discarded[len(discarded) - 2]) + '\n')
        # output.write('Remaining card: ' + str(discarded[len(discarded) - 1]) + '\n')

        n = int(stdin.readline().strip())
        # n = int(input.readline().strip())
    # print(time.time() - startTime)


main()
