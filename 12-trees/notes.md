# Tree

Tree is another form of Linked List that forks like so:

![Tree Forks](./tree-fork.png)

In a dict, the tree would have left and right nodes:

```python
{
    value: 4,
    left: {
        value: 3,
        left: None,
        right: None,
    },
    right: {
        value: 23,
        left: None,
        right: None,
    }
}
```

In above examples, these are binary trees. However, trees don't have to binary and can point to unlimted nodes. In binary trees, it is:

- `Full tree` if a node points to either two nodes or no node at all
- `Perfect tree` if all nodes is full/filled all the way across
- `Complete tree` if all nodes are full/filled from left to right

![Tree Terminology](./tree-terminology.png)

Every node in a tree can only have one `Parent`. Parent in binary trees can have two `Children`. If parents have no children, these nodes are a `leaf` like so:

![Tree Relationship](./tree-relationship.png)
