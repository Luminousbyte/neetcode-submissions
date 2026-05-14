class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        while self.q1:
            q1_x = self.q1.popleft()
            self.q2.append(q1_x)
        self.q1.append(x)

        while self.q2:
            q2_x = self.q2.popleft()
            self.q1.append(q2_x)
    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return True if not self.q1 else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()