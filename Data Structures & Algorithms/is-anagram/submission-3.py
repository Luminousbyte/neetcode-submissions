class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if len(s) == len(t) and s.count(s[i]) == t.count(s[i]) and set(s) == set(t):
                return True
        return False