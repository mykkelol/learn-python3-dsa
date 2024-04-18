class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_kth_from_end(self, k):
        if k <= 0:
            return None
        if k == 1:
            return self.tail
        slow = fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
    
    def partition_list(self, x):
        current = self.head
        if current is None:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next
        self.head = dummy1.next

    def remove_duplicates(self):
        if self.head is None:
            return None
        current = self.head
        prev = None
        values = set()
        while current:
            if current.value in values:
                prev.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                prev = current
            current = current.next

    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print(my_linked_list.find_middle_node().value)
print(my_linked_list.has_loop())
print(my_linked_list.find_kth_from_end().value)
print(my_linked_list.remove_duplicates())