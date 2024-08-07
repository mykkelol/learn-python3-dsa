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

def first_non_repeating_char(string):
    letters = {}

    for letter in string:
        letters[letter] = letters.get(letter, 0) + 1

    for letter in letters:
        if letters[letter] == 1:
            return letter
        
    return None

def group_anagrams(strings):
    groups = {}

    for string in strings:
        canonical = ''.join(sorted(string))
        
        if canonical in groups:
            groups[canonical].append(string)
        else:
            groups[canonical] = [string]
    
    return list(groups.values())

# return last index if duplicate found
def two_sum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment in nums_map:
            return [nums_map[compliment], i]
        nums_map[num] = i
    return []

# solve with prefix sum
# [1, 2, 3, 4, 5], 9 = [1, 3]
# [4, 5, 3, 2, 1], 11 = [1, 3]
def subarray_sum(nums, target):
    sum_index = {0 : -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []

def remove_duplicates(nums):
    return list(set(nums))

def has_unique_chars(str):
    return len(str) == len(set(str))

def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        compliment = target - num
        if compliment in set1:
            pairs.append((compliment, num))
    return pairs

def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest_sequence = 0

    for num in nums:
        if num - 1 not in nums_set:
            current_num = num
            current_sequence = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_sequence += 1

            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence