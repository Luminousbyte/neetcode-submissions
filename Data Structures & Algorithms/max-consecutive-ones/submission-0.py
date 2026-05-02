class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in nums:
            if i == 0:
                count = 0
                continue
            count += 1
            res = max(res, count)
        return res