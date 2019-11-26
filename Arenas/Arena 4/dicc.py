from sys import stdin

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def getIndex(self, hash, key):
        index = None
        for i in range(len(self.table[hash])):
            if self.table[hash][i][0] == key:
                index = i
        return index

    def getHash(self, key):
        index = hash(key) % self.size
        return index

    def insert(self, key, value):
        hash = self.getHash(key)
        self.table[hash].append((key, value))

    def get(self, key):
        hash = self.getHash(key)
        index = self.getIndex(hash, key)
        if index is None:
            return None
        return self.table[hash][index][1]

    def remove(self, key):
        hash = self.getHash(key)
        index = self.getIndex(hash, key)
        if index is not None:
            del(self.table[hash][index])

    def printht(self):
        print(self.table)

#import time
def main():
    instructions = int(stdin.readline().strip())
    #it = time.time()
    ht = HashTable(10000)
    #print('create table:', time.time() - it)
    #it = time.time()
    for i in range(instructions):
        instr = stdin.readline().strip().split()
        if instr[0] == 'ponga':
            ht.insert(instr[1], instr[2])
        elif instr[0] == 'busque':
            res = ht.get(instr[1])
            if res == None:
                #pass
                print(instr[1] + '?')
            else:
                #pass
                print(instr[1] + ' vale ' + res)
        else:
            ht.remove(instr[1])
    #print('procedure:', time.time() - it)


main()