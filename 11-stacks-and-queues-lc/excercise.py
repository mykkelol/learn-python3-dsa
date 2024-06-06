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