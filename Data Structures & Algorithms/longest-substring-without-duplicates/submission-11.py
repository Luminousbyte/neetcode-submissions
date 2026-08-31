class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left, max_l = 0, 0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            max_l = max(right - left + 1, max_l)
        
        return max_l