class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        store = []
        # calculate the min_stack for the values 
        if len(self.min_stack) == 0 : 
            self.min_stack.append(val)
            return None
        else : 
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
            

    def pop(self) -> None:
        store = []
        num = self.stack.pop()
        if num == self.min_stack[-1]:
            self.min_stack.pop()
            
        return None



    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
 
        
