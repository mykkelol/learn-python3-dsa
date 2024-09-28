# Heap

Heap is a binary search tree that has its numbers distributed in a different way where the highest value will always be at the top and its descendents (values less than or equal to) are at the bottom if it's a `max heap` or lowest value at the top if it's a `min heap`. For a binary search tree to be a heap, these conditions also must be met:

- a complete tree (i.e. every node must have both children)
- unlike regular trees, heaps can also have duplicated nodes (i.e. equal to)
- it doesn't matter where the lowest values are in the tree as long as it is a value less than or equal to its parents

This means that heaps are not great for searching, but it's great for keeping track of the highest values at the top and quickly remove it

# How heaps are stored

Heaps are stored in a list, so a **node class** isn't needed like trees. However, heaps only store integers in the list and said integers can be stored two ways:

- root at index 0
- root at index 1

### Root at index 1

![Heap at index 1](./heap-storing-index-1.png)

Since the heap integers are added to lists in a contiguous pattern, starting with index 1 makes the math simple. Examples:

- Finding left child: `2 * parent_index`
- Finding right child: `2 * parent_index + 1`
- Finding parent of left child: `child_index / 2` (assume index 6, then 3)
- Finding parent of right child: `child_index / 2` (assume index 7, then 3 since integer division drops .5 of 3.5)

### Root at index 0

When leading with index 0 for heaps, we'd need to move over one index. Below, notice in every equation, we simply moved one index from formulas used when leading with index 1:

```python
class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) + 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
```

# Insert value into heap

![Heap insert](./heap-insert.png)

In above heap, insertion can happen using `while` loop with the following (assume we want to insert 100 and 75):

- insert the value at the next contiguous index open even if the value is greater than the current parent (i.e. .append(100) which would be under 72)
- in the while loop, keep swapping with parent using integer division and exit when either these two conditions are met: top of the tree reached (i.e. index 1) or child is less than its parent

```python
    def _insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
```

# Remove value from heap

In heaps, three things happen when removing a value:

- Only the top of the tree is removed regardless if it's a max or a min heap
- When removing, the last index is swapped with the top of three
- After the last index is pushed to the top, `sink_down` helper method is used to rearrange the heap

```python
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(max_index)
            right_index = self._right_child(max_index)

            max_value = self._heap[max_index]
            left_value = self._heap[left_index]
            right_value = self._heap[right_index]

            """
            checking if the left index is less than the length of
            the list rather than checking if left index is not empty
            avoids IndexError
            """
            if (left_index < len(self.heap) and left_value > max_value):
                max_index = left_index

            if (right_index < len(self.heap) and right_value > max_value):
                max_index = right_index

            if max_index is not index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


    def _remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_heap = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_heap
```

# Priority Queue & Big O

Priority queue is when a specific condition is prioritized such as the highest priority queue is the max value that must be removed. Priority queue are great problems for heaps to use as a solution since removing the max value in a max heap is really efficient but
technically, all other data structures could be utilized as well for priority queues:

| Data Structure     | Big O | Description                                                                                                                                                              |
| ------------------ | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Linked List        | O(n)  | requires traversing through the entire linked list until the max value is reached                                                                                        |
| List               | O(n)  | similar issue as linked list                                                                                                                                             |
| Dictionary         | O(n)  | requires traversing through the keys. O(1) is achievable if max value is already known which is never the case in priority queue and is impossible                       |
| Binary Search Tree | O(n)  | could achieve log(n) like heap if the tree is balanced. But generally degrades to O(n) if the tree is unbalanced (when the tree keeps branching/appending the same path) |

Heap, on the other hand, allows priority queue to achieve O(log n). Unlike BST, which can become unbalanced, heaps are inherently complete/balanced. Thus, more efficient since traversing for insertion or extraction would only ever be as long as the height of the tree.
