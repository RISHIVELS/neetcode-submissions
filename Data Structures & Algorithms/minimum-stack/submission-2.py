class MinStack:

    def __init__(self):
        self.original_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.original_stack.append(val)
        if len(self.min_stack) == 0 : 
            self.min_stack.append(val)
        else : 
            last_value = self.min_stack[-1]
            if val <= last_value : 
                self.min_stack.append(val)
        

    def pop(self) -> None:
        if len(self.original_stack) == 0 : 
            return None
        else : 
            if self.min_stack[-1] == self.original_stack[-1]:
                self.min_stack.pop()
            return self.original_stack.pop()
        

    def top(self) -> int:
        if len(self.original_stack) == 0 : 
            return None
        else : 
            return self.original_stack[-1]        

    def getMin(self) -> int:
        if len(self.min_stack) == 0 : 
            return None
        else : 
            return self.min_stack[-1]      
        
