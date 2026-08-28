class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_n = ""
        for l in s:
            if l.isalnum():
                s_n += l.lower()
        x = "".join(reversed(s_n))
        return s_n == x
        