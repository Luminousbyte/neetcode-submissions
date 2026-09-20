class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = path.split("/")

        for cur in curr:
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "." and cur != "":
                stack.append(cur)
            
        return "/" + "/".join(stack)