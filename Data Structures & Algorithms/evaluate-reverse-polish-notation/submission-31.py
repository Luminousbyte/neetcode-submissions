class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                total = stack.pop() + stack.pop()
                stack.append(total)
            elif i == "*":
                total = stack.pop() * stack.pop()
                stack.append(total)
            elif i == "-":
                total = -stack.pop() + stack.pop()
                stack.append(total)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                total = int(b/a)
                stack.append(total)
            else:
                stack.append(int(i))
        return stack[0]