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
