class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lst = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            lst.append(word1[i])
            lst.append(word2[j])
            i += 1
            j += 1

        lst.append(word1[i:])
        lst.append(word2[j:])
        return "".join(lst)