class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(int)
        for value in nums:
            dic[value] += 1

        for val in dic.values():
            if val > 1:
                return True
        return False