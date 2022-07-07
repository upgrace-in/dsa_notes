# Dictionaries in Python are implemented using a data structure called hash table
# This method is incomplete becasue it doesnot handle collisions (listen, silent)
# To handle collisions:
'''
    While inserting a new key-value pair if the target index for a key is occupied by another key
    then we try the next index, followed by the next and so on till we the closest empty location
    Same goes for finding and updating
'''
MAX_HASH_TABLE_SIZE = 4096

def get_index(data_list, a_string):
    result = 0

    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number

    list_index = result % len(data_list)
    return list_index

class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None]*max_size

    def insert(self, key, value):
        ind = get_index(self.data_list, key)
        self.data_list[ind] = key, value

    def find(self, key):
        ind = get_index(self.data_list, key)
        kv = kv if self.data_list[ind] is None else self.data_list[ind]
        return kv[1]

    def update(self, key, value):
        ind = get_index(self.data_list, key)
        self.data_list[ind] = key, value

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]

h = HashTable()