class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        hashset = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if j == i:
                    continue
                if words[j] in words[i]:
                    hashset.add(words[j])
        return list(hashset)