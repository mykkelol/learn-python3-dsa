class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if len(self.stack1) == 0:
            return None
        else:
            return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0