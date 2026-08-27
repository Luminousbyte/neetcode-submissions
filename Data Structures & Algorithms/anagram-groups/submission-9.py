class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = defaultdict(list)
        for word in strs:
            diction["".join(sorted(word))].append(word)

        lst = []
        for v in diction.values():
            lst.append(v)
        
        return sorted(lst)