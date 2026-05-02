class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_str = {}
        for strings in strs:
            i = sorted(strings)
            new_str["".join(i)] = []


        for strings in strs:
            for key in new_str:
                if "".join(sorted(strings)) == key:
                    new_str[key].append(strings)

        new_lst = list(new_str.values())
        return new_lst