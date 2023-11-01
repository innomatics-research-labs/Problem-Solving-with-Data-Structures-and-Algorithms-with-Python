class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.stack))):
            self.stack[i] += val
