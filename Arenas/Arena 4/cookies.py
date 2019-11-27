from sys import stdin


class Heap:

    def __init__(self):
        self.heap = []
        self.heap_size = None

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def heapify(self, i):
        leftSon = self.left(i)
        rightSon = self.right(i)
        if leftSon <= self.heap_size and self.heap[leftSon] < self.heap[i]:
            largest = leftSon
        else:
            largest = i
        if rightSon <= self.heap_size and self.heap[rightSon] < self.heap[largest]:
            largest = rightSon
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def build_heap(self, A):
        self.heap = A
        self.heap_size = len(A) - 1
        for i in range(self.heap_size // 2, -1, -1):
            self.heapify(i)

    def rebuild(self):
        self.heap_size = len(self.heap) - 1
        for i in range(self.heap_size // 2, -1, -1):
            self.heapify(i)

    def getHeap(self):
        return self.heap

    def insert(self, el):
        self.heap.append(el)
        self.rebuild()

    def pop(self):
        elt = self.heap[0]
        del(self.heap[0])
        self.rebuild()
        return elt

    def heapSize(self):
        return len(self.heap)


def sweetness(a, k):
    heap = Heap()
    heap.build_heap(a)
    steps = 0
    smallerCookie = heap.pop()
    while smallerCookie < k:
        if heap.heapSize() == 0:
            return -1

        secondSmaller = heap.pop()
        newCookie = smallerCookie + (2 * secondSmaller)
        heap.insert(newCookie)
        steps += 1

        smallerCookie = heap.pop()

    return steps

# def sweetness(a, k):
#     steps = 0
#     a = sorted(a)
#     smallerCookie = a[0]
#     while smallerCookie < k:
#         if len(a) == 0:
#             return -1
#
#         secondSmaller = a[0]
#         newCookie = smallerCookie + (2 * secondSmaller)
#         a.append(newCookie)
#         steps += 1
#
#         a = sorted(a)
#         smallerCookie = a[0]
#
#     return steps



def main():
    inp = stdin.readline().strip()
    while inp != '':
        n, k = [int(x) for x in inp.split()]
        a = [int(x) for x in stdin.readline().strip().split()]

        print(sweetness(a, k))

        inp = stdin.readline().strip()


main()
