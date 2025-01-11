import heapq


class MinStack:

    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, val: int) -> None:
        heapq.heappush(self.data, val)
        self.size += 1

    def pop(self) -> None:
        if self.size > 0:
            self.size -= 1
            heapq.heappop(self.data)

    def top(self) -> int:
        if self.size > 0:
            return self.data[-1]

    def getMin(self) -> int:
        return self.data[0]


minStack = MinStack()
print(minStack.push(5))
print(minStack.push(0))
print(minStack.push(2))
print(minStack.push(4))
print(minStack.data)
# 0
print(minStack.getMin())
print(minStack.pop())
print(minStack.getMin())
print(minStack.pop())
print(minStack.getMin())
