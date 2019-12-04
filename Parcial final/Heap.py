class Heap:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def makeHeap(self, lista):
        self.heap = lista
        self.heap_size = len(lista) - 1
        for i in range(self.heap_size, -1, -1):
            self.heapify(i)

    def left(self, index):
        return int(index * 2 + 1)

    def right(self, index):
        return int(index * 2 + 2)

    def heapify(self, index):
        l = self.left(index)
        r = self.right(index)
        largest = index
        if l <= self.heap_size:
            if self.heap[index] < self.heap[l]:
                largest = l
        if r <= self.heap_size:
            if self.heap[largest] < self.heap[r]:
                largest = r
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)

    def printHeap(self):
        print(self.heap)


a = Heap()
a.makeHeap([1,2,3,4,5,7,81,6])
a.printHeap()

