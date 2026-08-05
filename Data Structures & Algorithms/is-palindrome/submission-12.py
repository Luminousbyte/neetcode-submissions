class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for ch in s:
            if ch.isalnum():
                s_new += ch.lower()
        
        i, j = 0, len(s_new)-1

        while i<=j:
            if s_new[i] != s_new[j]:
                return False
            i += 1
            j -= 1
        return True