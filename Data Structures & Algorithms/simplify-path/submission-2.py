class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        s = path.split("/")
        print(s)

        for i in s:
            if i == "..":
                if stack:
                    stack.pop()
            elif i != "" and i != ".":
                stack.append(i)

        return "/" + "/".join(stack)