# Big O

- way of comparing two sets of the same code mathematically to measure how efficent they run
- in programming, we measure efficiency through time complexity and space complexity (measures memory)
  - **Time Complexity** which measures the number of operations it takes to complete a task—doesn't measure time at all since finishing quicker doesn't mean it's efficient, just means we have better compute
  - **Space Complexity** which measures how much memory is consumed complete a task

# Omega, Theta, Omicron

When dealing with time and space complexity, we'll often see these greeks

- Omega (Ω) = best case
- Theta (θ) = average case
- Omicron (O) = worst case

These cases are seen even in the simplest programming. In this list, first index of nums is omega and index 6 is the Big O (folks often confuse omega as "best case" big O but big O is literally omicron)!

```python
nums = [1,2,3,4,5,6,7]
```

# Big O(n)

O of n is always a straight line that we call "proportional" and it's when we pass in `n` to run it `n` times. `n` times ran represents the number of operations

```python
# n
def print_nums(n):
    for i in range(n):
        # operation
        print(i)
```

# Drop Constants

One of few ways to simplify big O notation, drop constants is when `n + n = 2n` like below function and one would expect to write it as `O(2n)` but in actuality, the constant is dropped and it remains `O(n)`

```python
def print_nums(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
```

# Big O(n^2)

In the following function, `print_nums(10)` would run 100 operations since it's double loop or `n * n = n^2` or `O(n^2)`

```python
def print_nums(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

The graph below shows that `O(n^2)` is much steeper than `O(n)`. In plain english, this means that `O(n^2)` is much less efficient than `O(n)` from time complexity standpoint

![big_o_comparison](./big_o_comparison.png)
