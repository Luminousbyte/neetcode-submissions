class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                res = stack.pop() + stack.pop()
                stack.append(res)
            elif i == "-":
                first = stack.pop()
                sec = stack.pop()
                res = sec - first
                stack.append(res)
            elif i == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif i == "/":
                first = stack.pop()
                sec = stack.pop()
                res = sec/first
                stack.append(int(res))
            else:
                stack.append(int(i))
        return stack[0]