# Linked List

Linked list is a dynamic data structure consisting of a collection of nodes that have its own reference/link that contains data which together represent a sequence. It's not the same as a list and can be much more efficient since it can achieve O(1) when inserting or deleting at the beginning or the middle of a linked list, while list can only achieve O(1) if it's at the end of the list

![linkedlist_v_list](./linkedlist_v_list.png)

In the memory space above, notice while the **list** has all its elements stored in contiguous memory locations that are squential and accessible by indexes, the **linked list** consist of nodes that are scattered in memory with no indexes with links that connect them together

# LL in Big O

Linked list can achieve effciency for certain scenarios. For example:

- _append to end is_ `O(1)` since there's only one operation
- _append to start is_ `O(1)`
- _remove to end is_ `O(n)` since iteration is needed to repoint the last node as the new tail
- _append or remove from mid is_ `O(n)` due to iteration
- _lookup is_ `O(n)` due to iteration for both the index and the value. This differs from list since it can be O(1) when looking by index

![Big O in Linked List](./linkedlist_big_o.png)
