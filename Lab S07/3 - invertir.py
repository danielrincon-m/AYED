# Linked List Node definition
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


# Linked List definition
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def printList(self):
        current = self.head
        while current != None:
            if current.getData() is not None:
                print(current.getData(), end=' ')

            current = current.getNext()

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def getHead(self):
        return self.head

    def setHead(self, newHead):
        self.head = newHead

    def remove(self, item):
        try:
            current = self.head
            previous = None
            found = False
            while current != None and not found:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()

            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        except:
            return -1


def invertLinkedList(lili):
    if lili.size() > 1:
        first = lili.getHead()
        second = first.getNext()
        third = second.getNext()
        first.setNext(None)
        while second != None:
            second.setNext(first)
            first = second
            second = third
            if third != None:
                third = third.getNext()
        lili.setHead(first)
    return lili


def main():
    lili = LinkedList()
    elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for elt in elements:
        lili.add(elt)
    print('Lista original')
    lili.printList()
    lili = invertLinkedList(lili)
    print('\nLista invertida')
    lili.printList()


main()
