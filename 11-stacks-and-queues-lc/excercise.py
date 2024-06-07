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