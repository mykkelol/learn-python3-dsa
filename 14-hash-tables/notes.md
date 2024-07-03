# Hash Tables

Hash is a method/function that accepts a dictionary, storing it into a hash table with a designated `address` that it returns. Hash has two characteristics:

- `One way` - meaning if we pass a key-value pair, hash will return an adress but if we pass said address, the key-value will not be returned
- `Deterministic` - means an address will be returned for every pair passed

In the example below, we can pass `{"nails": 1000}` into the hash `set_items(key, value)` function like so:

![Hash Function](./hash-function.png)

The hash function adds the pair as a list and returns an address. To retrieve the value, we can do `get_item('screws')` and since hash are deterministic, we have the address to easily retrieve the value of screws which is 800.

**Note**: each address can contain more than a single pair. To retrieve the quantity of nuts, we'd need to loop through address 2
