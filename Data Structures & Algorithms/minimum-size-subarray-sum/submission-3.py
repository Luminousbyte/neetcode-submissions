class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_length = len(nums)
        l, r = 0, 1
        while l<r and r <= len(nums):
            if nums[l] == target:
                return 1
            if sum(nums[l:r]) < target:
                r += 1
            if sum(nums[l:r]) >= target:
                length = r-l
                min_length = min(min_length, length)
                l += 1
        return min_length