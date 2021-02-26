from LinkedList import LinkedList


class HashTable:
    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    def create_arr(self, size):
        # This function uses the map method to generate an arrat of linkedlists
        return list(map(lambda x: LinkedList(), [None] * size))

    def hash_func(self, key):
        # This function is the logic to generate a key to store the item in a linked list, it uses ord and % to loop through the list if the letter key[0] is larger than self.size
        return (ord(key[0]) - ord('a')) % self.size

