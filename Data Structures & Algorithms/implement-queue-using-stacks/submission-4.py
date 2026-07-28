class MyQueue:

    def __init__(self):
        self.original_stack = []
        self.queue_stack = []

    def push(self, x: int) -> None:
        self.original_stack.append(x)

    def pop(self) -> int:
        if len(self.queue_stack) == 0 : 
            while len(self.original_stack) != 0 : 
                last_element = self.original_stack.pop()
                self.queue_stack.append(last_element)
            return self.queue_stack.pop()
        else : 
            return self.queue_stack.pop()

    def peek(self) -> int:
        if len(self.queue_stack) == 0 : 
            while len(self.original_stack) != 0 : 
                last_element = self.original_stack.pop()
                self.queue_stack.append(last_element)
            return self.queue_stack[-1]
        else : 
            return self.queue_stack[-1] 

    def empty(self) -> bool:
        if len(self.queue_stack) !=0  or len(self.original_stack) != 0 : 
            return False 
        else : 
            return True 



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()