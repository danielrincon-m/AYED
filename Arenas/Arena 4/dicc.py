from sys import stdin
class HashNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        self.table = [None for _ in range(101)]

    def hash(self, key):
        # Generate hash from key.
        # Time O(N), Space O(1), where N is the length of key.
        hashed = 0
        for i in range(len(key)):
            hashed = (256 * hashed + ord(key[i])) % 101
        return hashed

    def add(self, key, value):
        # Add key, value.
        # Time O(1), Space O(1), where N is the num of elements in hashtable.
        bucket = self.hash(key)
        self.table[bucket] = HashNode(key, value)

    def find(self, key):
        # Find value from key.
        # Time O(1), Space O(1), where N is the num of elements in hashtable.
        bucket = self.hash(key)
        if not self.table[bucket]:
            return False
        else:
            temp = self.table[bucket]
            while temp:
                if temp.key == key:
                    return temp.value
                temp = temp.next
            return False

    def delete(self, key):
        # Delete key, value.
        # Time O(1), Space O(1), where N is the num of elements in hashtable.
        bucket = self.hash(key)
        if not self.table[bucket]:
            return False
        else:
            if self.table[bucket].key == key:
                self.table[bucket] = None
            else:
                temp = self.table[bucket]
                while temp:
                    if temp.next.key == key:
                        temp.next = temp.next.next
                        return
                    temp = temp.next
                return False

# import time
def main():
    # f = open('in.txt', 'r')
    instructions = int(stdin.readline().strip())
    # instructions = int(f.readline().strip())
    # it = time.time()
    ht = HashTable()
    # print('create table:', time.time() - it)
    # it = time.time()
    for i in range(instructions):
        instr = stdin.readline().strip().split()
        # instr = f.readline().strip().split()
        if instr[0] == 'ponga':
            ht.add(instr[1], instr[2])
        elif instr[0] == 'busque':
            res = ht.find(instr[1])
            if res == False:
                # pass
                print(instr[1] + '?')
            else:
                # pass
                print(instr[1] + ' vale ' + res)
        else:
            ht.delete(instr[1])
    # print('procedure:', time.time() - it)


main()