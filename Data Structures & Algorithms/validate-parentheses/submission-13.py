class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = { ")":"(",
                        "}":"{",
                        "]":"[" }
        for bracket in s:
            if bracket in closetoopen:
                if stack and closetoopen[bracket] == stack[-1]:
                    stack.pop()
                    continue
                return False
            stack.append(bracket)
        return True if not stack else False
            