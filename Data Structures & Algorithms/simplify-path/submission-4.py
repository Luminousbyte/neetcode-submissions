class Solution:
    def simplifyPath(self, path: str) -> str:
        l_path = path.split("/")
        stack = []
        for i in l_path:
            if i == "..":
                if stack:
                    stack.pop()
            elif i != "" and i != ".":
                stack.append(i)
        print(stack)
        return "/" + "/".join(stack)