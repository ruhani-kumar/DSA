class MinStack:

    def __init__(self):
        self.st = []
        self.min = []

    def push(self, value: int) -> None:
        self.st.append(value)
        '''if len(self.st) == 1:
            self.min.append(value)
        elif value<=self.min[-1]:
            self.min.append(value)'''
        if len(self.min) == 0 or value <= self.min[-1]:
            self.min.append(value)

    def pop(self) -> None:
        top = self.st.pop()
        if top == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()