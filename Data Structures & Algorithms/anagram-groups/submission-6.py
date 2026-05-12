class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = set()
        for w in strs:
            hashset.add("".join(sorted(w)))
        
        hashmap = defaultdict(List)
        for w in hashset:
            hashmap[w] = []

        for w in strs:
            x = "".join(sorted(w))
            hashmap[x].append(w)

        lst = []
        for val in hashmap.items():
            lst.append(val[1])
        lst.sort(key = len)
        
        return lst