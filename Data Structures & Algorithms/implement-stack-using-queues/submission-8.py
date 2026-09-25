class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.queue2.insert(0, x)

    def pop(self) -> int:
        return self.queue2.popleft()

    def top(self) -> int:
        return self.queue2[0]

    def empty(self) -> bool:
        return True if not self.queue2 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()