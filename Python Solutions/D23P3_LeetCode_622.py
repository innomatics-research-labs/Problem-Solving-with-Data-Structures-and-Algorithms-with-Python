from collections import deque
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = deque()
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        else:
            return False
        
    def deQueue(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.queue:
            return -1
        else:
            return self.queue[0]
        
    def Rear(self) -> int:
        if not self.queue:
            return -1
        else:
            return self.queue[-1]
        
    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        if len(self.queue) == self.size:
            return True
        else:
            return False
