class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = { ")":"(",
                        "}":"{",
                        "]":"[" }
        for b in s:
            if b in closetoopen:
                if stack and closetoopen[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        print(stack)
        return stack == []