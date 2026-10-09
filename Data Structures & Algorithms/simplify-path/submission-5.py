class Solution:
    def simplifyPath(self, path: str) -> str:
        path_l = path.split("/")
        stack = []
        for l in path_l:
            
            if l == "..":
                if stack:
                    stack.pop()
            elif l != "" and l != ".":
                stack.append(l)
        # print(stack)
        return "/" + "/".join(stack)