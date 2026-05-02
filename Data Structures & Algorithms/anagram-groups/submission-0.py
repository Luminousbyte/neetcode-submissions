class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diction = {}
        for i in range(len(strs)):
            diction[''.join(sorted(strs[i]))] = []

        for i in diction.keys():
            for j in strs:
                if "".join(sorted(j)) == i:
                    diction[i].append(j)

        listed = []
        for i in diction:
            listed.append(diction[i])

        listed.sort()
        return listed