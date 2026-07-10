class HashTable:

    def __init__(self):
        self.collection = {}

    def hash(self, string: str):
        sum = 0
        for char in string:
            sum += ord(char)
        return sum

    def add(self, add_key, value):
        new_key = self.hash(add_key)
        if new_key not in self.collection:
            self.collection[new_key] = {}
        self.collection[new_key][add_key] = value

    def remove(self, remove_key):
        new_key = self.hash(remove_key)
        if new_key in self.collection and remove_key in self.collection[new_key]:
            del self.collection[new_key][remove_key]

    def lookup(self, lookup_key):
        new_key = self.hash(lookup_key)
        if new_key in self.collection and lookup_key in self.collection[new_key]:
            return self.collection[new_key][lookup_key]
        
        return None