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

A more common recursive case is factorial, where n input returns the product of the numbers before or equal to n:

```python
def factorial(n):
    if n === 1:
        return 1
    return n * factorial(n - 1)
```

The call stack for factorial would return 1, 2, 6, and finally 24
