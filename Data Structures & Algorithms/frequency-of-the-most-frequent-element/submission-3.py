class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        for i in range(len(nums)):
            j = i - 1
            tempk = k
            while j>=0 and (tempk - (nums[i] - nums[j])) >= 0:
                tempk -= (nums[i] - nums[j])
                j -= 1
            res = max(res, i-j)
        return res