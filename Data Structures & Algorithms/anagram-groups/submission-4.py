class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for c in strs:
            sort_c = "".join(sorted(c))
            dictionary[sort_c] = []

        for keys in dictionary:
            for c in strs:
                sort_c = "".join(sorted(c))
                if sort_c == keys:
                    dictionary[sort_c] .append(c)
        
        lst = []

        for i in dictionary.values():
            lst.append(i)

        return lst