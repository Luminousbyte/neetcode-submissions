class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i].lstrip("-").isnumeric():
                stack.append(int(operations[i]))
            elif operations[i] == "D":
                double = 2 * stack[-1]
                stack.append(double)
            elif operations[i] == "C":
                stack.pop()
            else:
                addition = stack[-1] + stack[-2]
                stack.append(addition)
        return sum(stack)