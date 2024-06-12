class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)
    
    def pop(self):
        if len(self.stack_list) == 0:
            return None
        else:
            return self.stack_list.pop()
        
    def size(self):
        return len(self.stack_list)
        
    def is_empty(self):
        return self.size(self.stack_list) == 0
    
    def print_stack(self):
        for i in self.stack_list:
            print(i)
        
def is_balanced_parentheses(parens):
    stack = Stack()
    for p in parens:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

def reverse_string(my_string):
    stack = Stack()
    reversed_string = ''

    for c in my_string:
        stack.push(c)

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

def sort_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())