class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = []
        for word in s.split(" "):
            lst.append(word)

        if len(pattern) != len(lst):
            return False

        hashset_pattern = set(pattern)
        hashset_s = set(lst)

        print(hashset_pattern)
        print(hashset_s)

        return len(hashset_pattern) == len(hashset_s)

