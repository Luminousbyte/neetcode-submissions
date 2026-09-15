class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i.lstrip("-").isdigit():
                stack.append(int(i))
            if i == "+":
                stack.append((stack[-1] + stack[-2]))
            if i == "C":
                stack.pop()
            if i == "D":
                d = stack[-1]*2
                stack.append(d)
            print(stack)
        return sum(stack)