class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for l in s:
            if l.isalnum():
                s_new += l.lower()
        
        l, r = 0, len(s_new)-1
        while l<=r:
            if s_new[l] != s_new[r]:
                return False
            l += 1
            r -= 1
        return True