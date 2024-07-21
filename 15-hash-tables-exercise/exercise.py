class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return None
    
    def get_keys(self):
        all_keys = []
        for address in self.data_map:
            if address is not None:
                for item in address:
                    all_keys.append(item[0])
        return all_keys

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
      

def item_in_common(list1, list2):
    items = {}
    for i in list1:
        items[i] = True
    for j in list2:
        if j in items:
            return True
    return False

def find_duplicates(nums):
    numbers = {}
    duplicates = []

    for n in nums:
        if n in numbers:
            if numbers.get(n) == 1:
                duplicates.append(n)
            numbers[n] += 1
        else:
            numbers[n] = 1
    
    return duplicates