class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    # [2, 4, 1] entry = 3
    def push(self, entry):
        self.stack.append(entry)
        entry = min(entry, self.min_stack[-1] if self.min_stack else entry)
        self.min_stack.append(entry)
    
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
