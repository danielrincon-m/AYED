# Linked List Node definition
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.prev = None
        self.next = None

    def getData(self):
        return self.data

    def getPrev(self):
        return self.prev

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setPrev(self, newprev):
        self.prev = newprev

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
        if self.head != None:
            self.head.setPrev(node)
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
            if current.getPrev() != None:
                print('prev =', current.getPrev().getData(), end=', ')
            else:
                print('prev =  ', end=', ')
            if current.getData() is not None:
                print('current =', current.getData(), end=', ')
            if current.getNext() != None:
                print('next =', current.getNext().getData())
            else:
                print('next =  ')

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

    def getTail(self):
        current = self.head
        next = current.getNext()
        while next != None:
            current = next
            next = current.getNext()
        return current

    def remove(self, item):
        try:
            current = self.head
            previous = None
            next = None
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
                current.getNext().setPrev(previous)
        except:
            return -1


def join(lili1 : LinkedList, lili2 : LinkedList):
    tail = lili1.getTail()
    head = lili2.getHead()
    tail.setNext(head)
    head.setPrev(tail)
    return lili1


def main():
    lili = LinkedList()
    lili2 = LinkedList()

    #Insertar un nuevo elemento
    elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(elements) - 1, -1, -1):
        lili.add(elements[i])
    lili.printList()
    print()

    #Eliminar un elemento
    lili.remove(5)
    lili.printList()
    print()

    #Unir dos listas
    for elt in elements:
        lili2.add(elt)
    joinedlili = join(lili, lili2)
    joinedlili.printList()


main()
