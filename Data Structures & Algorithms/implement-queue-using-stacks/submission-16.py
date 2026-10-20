class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        while self.stack2:
            self.stack2.pop()
        for i in range(len(self.stack1)-1, -1, -1):
            self.stack2.append(self.stack1[i])

    def pop(self) -> int:
        x = self.stack2.pop()
        self.stack1.remove(x)
        return x

    def peek(self) -> int:
        return self.stack2[-1]

    def empty(self) -> bool:
        return self.stack2 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()