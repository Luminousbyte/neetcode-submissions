class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1

        r = len(s) - 1
        while r >= 0 and s[r] == " ":
            r -= 1
        
        l = r-1

        while l >= 0 and s[l] != " ":
            l -= 1
        
        return (r - l)