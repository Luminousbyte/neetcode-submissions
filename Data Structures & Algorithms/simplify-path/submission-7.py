class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split("/")
        stack = []
        for c in p:
            if stack and c == "..":
                stack.pop()
            elif c != "" and c != "." and c != "..":
                stack.append(c)
        return ("/" + "/".join(stack))