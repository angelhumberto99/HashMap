# hashing functions
def hash_str(key):
    if isinstance(key, int):
        return key

    result = 5381
    for char in key:
        result = 33 * result + ord(char)
    return result

def pjw_hashing(key):
    if isinstance(key, int):
        return key
    h = 0
    g = 0
    for char in key:
        h = (h << 4) + ord(char)
        g = h & 0xF
        if g > 1:
            h = h ^ (g << 24)
            h = h ^ g
    return h

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"\n\t{self.key}: {self.value}\n".expandtabs(4)

class HashMap:
    def __init__(self, hashing_function = hash_str, max_length = 16):
        self.__max_length = max_length
        self.__container = [None for _ in range(self.__max_length)]
        self.__hashing_function = hashing_function

    def __str__(self):
        """Returns a formatted string that represents the contents of the hash map"""
        keys = self.get_keys()
        length = len(keys)
        if length == 0: return "[]"

        # format string
        str = "[\n"
        for i, v in enumerate(keys):
            comma = '' if i + 1 == length else ','
            str += f"\t{{{self.__get(v)}\t}}{comma}\n".expandtabs(2)
        str += "]"

        return str
    
    def add(self, key, value):
        """Adds a new key/value pair to the container"""
        hash = self.__hashing_function(key) % self.__max_length
        # create an inverse list if the postition is None
        if self.__container[hash] is None:
            self.__container[hash] = [Node(key, value)]
        # append the new value to the inverse list
        else:
            self.__container[hash].append(Node(key, value))

    def __get(self, key):
        """Returns the key/value pair if exists"""
        hash = self.__hashing_function(key) % self.__max_length
        if self.__container[hash] is None: return None
        for i in self.__container[hash]:
            if i.key == key: return i
        return None
    
    def get(self, key):
        """Returns the value if exists"""
        el = self.__get(key)
        return el.value if el is not None else None

    def get_keys(self):
        """Returns all the keys in the container"""
        # removes all None positions in the container
        filtered_list = list(filter(lambda x: x is not None, self.__container))
        keys = []
        # appends all the keys in the list
        for inversed_list in filtered_list:
            for j in inversed_list:
                keys.append(j.key)
        return keys

    def remove(self, key):
        """Removes element if exists in the container"""
        # find element
        element = self.__get(key)
        if element is None: return

        # remove from container        
        hash = self.__hashing_function(key) % self.__max_length
        self.__container[hash].remove(element)

        # set value to None if the position is an empty list
        if len(self.__container[hash]) == 0:
            self.__container[hash] = None