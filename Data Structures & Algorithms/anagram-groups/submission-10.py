class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = defaultdict(list)
        for word in strs:
            diction["".join(sorted(word))].append(word)

        return list(diction.values())