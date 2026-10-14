class Solution:
    def isValid(self, s: str) -> bool:
        seen = {"}":"{",
                "]":"[",
                ")":"("}
        stack = []
        for b in s:
            if b in seen:
                if stack and seen[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
            # print(stack)
        return stack == []