class MinStack:

    def __init__(self):
        self.stk = []
        self.smStk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.smStk:
            smaller = val
        else:
            smaller = min(val, self.smStk[-1])
        self.smStk.append(smaller)

    def pop(self) -> None:
        self.stk.pop()
        self.smStk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.smStk[-1]
        
