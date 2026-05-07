class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        lst = []
        for w in strs[0]:
            lst.append(w)
        print(f"lst before:",lst)
        for r in range(len(strs)):
            for c in range(len(lst)):
                if strs[r][c] != lst[c]:
                    lst[c] = 0
        print(f"lst after:",lst)
        s = ""
        for i in lst:
            if i == 0:
                break
            s += i
        return s