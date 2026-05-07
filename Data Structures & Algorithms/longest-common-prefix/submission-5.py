class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        print(strs)
        min_length = len(strs[0])
        
        
        lst = []
        for w in strs[0]:
            lst.append(w)
        print(f"lst before:",lst)
        for r in range(len(strs)):
            for c in range(min_length):
                if lst[c] != strs[r][c]:
                    lst[c] = 0
        print(f"lst after:",lst)
        s = ""
        for i in lst:
            if i == 0:
                break
            s += i
        return s