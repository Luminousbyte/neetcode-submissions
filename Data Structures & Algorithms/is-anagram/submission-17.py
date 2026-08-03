class Solution:
    def isAnagram(self, s: str, t: str) -> bool:     
        if len(s) != len(t):
            return False
        dict1, dict2 = defaultdict(int), defaultdict(int)
        for i in s:
            dict1[i] += 1
        for j in t:
            dict2[j] += 1
        return dict1 == dict2