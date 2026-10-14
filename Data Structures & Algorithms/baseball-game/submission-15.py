class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "+":
                total = stack[-1] + stack[-2]
                stack.append(total)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                total = stack[-1]*2
                stack.append(total)
            else:
                stack.append(int(operations[i]))
        return sum(stack)