# Heap

Heap is a binary search tree that has its numbers distributed in a different way where the highest value will always be at the top and its descendents (values less than or equal to) are at the bottom if it's a `max heap` or lowest value at the top if it's a `min heap`. For a binary search tree to be a heap, these conditions also must be met:

- a complete tree (i.e. every node must have both children)
- unlike regular trees, heaps can also have duplicated nodes (i.e. equal to)
- it doesn't matter where the lowest values are in the tree as long as it is a value less than or equal to its parents

This means that heaps are not great for searching, but it's great for keeping track of the highest values at the top and quickly remove it

# How heaps are stored

Heaps are stored in a list, so a node class isn't needed like trees. However, heaps only store integers in the list and said integers can be stored two ways:

- root at index 0
- root at index 1

### Root at index 1

![Heap at index 1](./heap-storing-index-1.png)

### Root at index 0
