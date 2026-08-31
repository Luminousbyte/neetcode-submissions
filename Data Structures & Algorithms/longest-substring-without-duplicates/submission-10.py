class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l, r = 0, 0
        max_len = 0
        while r<len(s):
            if s[r] in charset:
                charset.remove(s[l])
                l += 1
            else:
                charset.add(s[r])
                max_len = max(r-l+1, max_len)
                r += 1
        return max_len