class MinStack:

    def __init__(self):
        self.smallest_upto = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        smallest = self.smallest_upto[-1] if self.smallest_upto else val
        if val < smallest:
            self.smallest_upto.append(val)
        else:
            self.smallest_upto.append(smallest)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.smallest_upto.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest_upto[-1]
        
