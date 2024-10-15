# Recursion

A function that calls itself until it doesn't. It's like opening a nested gift box over and over until the last box.

```python
def open_gift_box():
    if ball:
        return ball
    open_gift_box()
```

- `Base Case` - returning and exiting the function from calling itself again or returning the ball is the base case
- `Recursive Case` - in above psuedo, the function calling itself again is the recursive case
- `Stack Overflow` - when the recursive function loops infitely without a base case

# Call Stack

The following example demonstrates a `call stack` with non-recursive functions, which is the exact same concept in a LIFO [stacks](../09-stacks-and-queues/notes.md):

```python
def funcThree():
    print('three')

def funcTwo():
    funcThree()
    print('two')

def funcOne():
    funcTwo()
    print('one')

funcOne()

# returns the following in exact order (i.e. LIFO):
# three
# two
# one
```
