from sys import stdin


class Heap:
    def __init__(self, policy):
        self.heap = []
        self.heap_size = None
        self.policy = policy #True: max-heap; False: min-heap

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def heapify (self, i):
        if self.policy is True:
            self.max_heapify(i)
        else:
            self.min_heapify(i)

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.heap[l] < self.heap[i]:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and self.heap[r] < self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def build_heap(self, A):
        self.heap = A
        self.heap_size = len(A) - 1
        for i in range(self.heap_size, -1, -1):
            self.heapify(i)

    def getHeap(self):
        return self.heap

    def insert(self, el):
        self.heap.append(el)
        self.build_heap(self.heap)

    def delete(self, index):
        self.build_heap(self.heap[:index]+self.heap[index+1:])

    def update(self, index, newVal):
        self.heap[index] = newVal
        self.build_heap(self.heap)

def entrada():
    return [int(x) for x in stdin.readline().strip().split()]

def main():
    lista = entrada()

    heap = Heap(True)
    heap.build_heap(lista)
    print(heap.getHeap())

    heap = Heap(False)
    heap.build_heap(lista)
    print(heap.getHeap())


main()
