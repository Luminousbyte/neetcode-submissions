class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if stack:
                if i == "+":
                    stack.append((stack.pop() + stack.pop()))
                elif i == "-":
                    stack.append((-stack.pop() + stack.pop()))
                elif i == "*":
                    stack.append((stack.pop() * stack.pop()))
                elif i == "/":
                    a = stack.pop()
                    b = stack.pop()
                    total = int(b/a)
                    stack.append(total)
                else:
                    stack.append(int(i))
            else:
                stack.append(int(i))
        return stack[0]