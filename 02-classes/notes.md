# Classes

Method of programming to model or construct process or things in the world with a goal of encapsulating them into logical, hierarchy groupings. In short, classes are blueprints, recipes, or specifications that encapsulates methods and attributes into private (`_get_next()`) or public (`append()`) methods and attributes, making abstraction possible by privatizing/abstracting certain methods or attributes. With class or "blueprint", we can then create multiple instances (`my_linked_list`) of it

```python
class LinkedList:
    def __init__(self, data):
        self.data = data

    def append(self):
        pass

    def _get_next(self):
        pass

my_linked_list = new LinkedList('hi')
my_linked_list1 = new LinkedList('hi')
```

# Pointer

Values of any variables defined in programming are all stored in the memory and pointer is a concept that allows us to point variables to these values in the memory. Some data types, such as `int`, are immutable while others (see `num2`), such as `dict`, are not. This means that the moment we store 11 in the memory, we cannot change its address in the memory whereas we could with `dict`

```python
num1 = 11
num2 = num1

print('Before num2 value is updated')
print('num1 = ', num1)
print('num2 = ', num2)
print('')
print('num1 points to:', id(num1))
print('num2 points to:', id(num2)) # same as num1

num2 = 22

print('After num2 value is updated')
print('num1 = ', num1)
print('num2 = ', num2)
print('')
print('num1 points to:', id(num1))
print('num2 points to:', id(num2)) # diff from num1
```

In the following, if `{'value': 11}` is overriden in both dicts, python dumps the address `{'value': 11}` in **garbage collection**

```python
dict1 = {'value': 11}
dict2 = dict1

print('Before dict2 value is updated')
print('dict1 = ', dict1)
print('dict2 = ', dict2)
print('')
print('dict1 points to:', id(dict1))
print('dict2 points to:', id(dict2)) # same as dict1

dict2 = dict2['value'] = 22

print('After dict2 value is updated')
print('dict1 = ', dict1)
print('dict2 = ', dict2)
print('')
print('dict1 points to:', id(dict1))
print('dict2 points to:', id(dict2)) # same as dict1
```
