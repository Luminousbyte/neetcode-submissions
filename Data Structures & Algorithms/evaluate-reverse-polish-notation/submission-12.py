class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                val = val2 + val1
                stack.append(val)
            if i == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                val = val2 - val1
                stack.append(val)
            if i == "/":
                val1, val2 = stack.pop(), stack.pop()
                val = val2/val1
                print(val)
                print(int(val))
                stack.append(int(val))
            if i == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                val = val2 * val1
                stack.append(val)
            if i.lstrip("-").isdigit():
                stack.append(int(i))
        return stack[-1]