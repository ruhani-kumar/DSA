class MinStack:

    '''def __init__(self):
        self.st = []
        self.min = []

    def push(self, value: int) -> None:
        self.st.append(value)
        if len(self.st) == 1:
            self.min.append(value)
        elif value<=self.min[-1]:
            self.min.append(value)
        //if len(self.min) == 0 or value <= self.min[-1]:
            self.min.append(value)//

    def pop(self) -> None:
        top = self.st.pop()
        if top == self.getMin():
            self.min.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min[-1]'''
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.getMin():
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()