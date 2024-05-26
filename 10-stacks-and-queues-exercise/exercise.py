class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_list(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next