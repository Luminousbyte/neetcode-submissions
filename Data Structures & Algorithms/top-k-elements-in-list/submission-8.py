class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = {}
        for i in nums:
            diction[i] = nums.count(i)

        lst = []
        for i in diction.values():
            lst.append(i)

        lst.sort()
        x = lst[-k:]

        result = [j for j, v in diction.items() if v in x]

        return result