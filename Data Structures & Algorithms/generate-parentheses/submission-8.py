class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s):
            count = 0
            for i in s:
                if i == "(":
                    count += 1
                if i == ")":
                    count -= 1
                if count < 0:
                    return False
            return not count
        def dfs(s):
            if len(s) == n*2:
                if valid(s):
                    res.append(s)
                return
            dfs(s + "(")
            dfs(s + ")")
        dfs("")
        return res