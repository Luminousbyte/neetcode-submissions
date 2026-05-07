class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key= len)

        res = ""
        for c in range(len(strs[0])):
            for r in range(1, len(strs)):
                if strs[r][c] != strs[0][c]:
                    return res
            res += strs[0][c]
        print(res)
        return res