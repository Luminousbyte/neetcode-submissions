class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                val = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif i == "*":
                val = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif i == "-":
                val = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif i == "/":
                val = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(val))
            else:
                stack.append(int(i))
        return stack[-1]