# Doubly Linked List

Doubly linked list is just a singular linked list with pointers that also goes backwards and thus, necessitates `self.prev` in DLL nodes.

![Doubly Linked List](./doubly_linked_list.png)

In DLL constructors and DLL node constructor, not much change except again, reverse pointers:

```python
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    class DoubleLinkedList:
        def __init__(self, value):
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 0
```

# Doubly Linked List Append

Doubly linked list append is similar to singular linked list with exception that after appending, the new node needs to set previous to the current tail through `new_node.prev = self.tail` prior to setting itself as the tail

```python
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev =  self.tail
            self.tail = new_node
        self.length += 1
        return True
```
