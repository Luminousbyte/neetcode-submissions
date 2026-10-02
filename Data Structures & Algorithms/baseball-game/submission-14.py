class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "+":
                total = stack[-1] + stack[-2]
                stack.append(total)
            elif i == "C":
                stack.pop()
            elif i == "D":
                dobl = stack[-1]*2
                stack.append(dobl)
            else:
                stack.append(int(i))
        return sum(stack)