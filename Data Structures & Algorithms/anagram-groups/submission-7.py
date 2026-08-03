class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        for s in strs:
            n = "".join(sorted(s))
            dct[n].append(s)
        lst = []
        for k in dct.values():
            lst.append(k)
        return sorted(lst)