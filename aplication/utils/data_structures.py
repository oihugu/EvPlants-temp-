class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        self.stack.append(dataval)
        
    def remove(self):
        if len(self.stack) <= 0:
            raise()
        else:
            return self.stack.pop()