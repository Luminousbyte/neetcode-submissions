class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()
                
                n = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n

                stack.append(int(n) * substring)
        return "".join(stack)