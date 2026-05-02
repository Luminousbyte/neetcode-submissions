class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            val = abs(ord(s[i]) - ord(s[i-1]))
            print(val)
            res += val
        return res