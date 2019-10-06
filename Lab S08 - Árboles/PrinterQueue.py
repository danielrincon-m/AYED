from sys import stdin


class Queue:
    def __init__(self, items, checkIndex):
        self.checkIndex = checkIndex
        self.time = 0
        self.priorities = items

    def removeElement(self):
        value = self.priorities[0]
        del(self.priorities[0])
        self.checkIndex -= 1
        if all(i <= value for i in self.priorities):
            self.time += 1
        else:
            self.priorities.append(value)
            if self.checkIndex == -1:
                self.checkIndex = len(self.priorities) - 1

    def printed(self):
        return True if self.checkIndex < 0 else False

    def getTime(self):
        return self.time


def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        size, pos = [int(x) for x in stdin.readline().strip().split()]
        values = [int(x) for x in stdin.readline().strip().split()]
        queue = Queue(values, pos)
        while not queue.printed():
            queue.removeElement()
        print(queue.getTime())


main()
