class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)

        shortest = strs[0]
        res = ""

        for c in range(len(shortest)):
            ch = shortest[c]

            for r in range(1, len(strs)):
                if strs[r][c] != ch:
                    return res

            res += ch

        return res