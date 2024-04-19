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
