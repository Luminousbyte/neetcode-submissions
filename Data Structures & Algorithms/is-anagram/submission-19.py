class Solution:
    def isAnagram(self, s: str, t: str) -> bool:     
        if len(s) != len(t):
            return False
        s1, s2 = defaultdict(int), defaultdict(int)

        for i in s:
            s1[i] += 1
        for j in t:
            s2[j] += 1
        return s1 == s2