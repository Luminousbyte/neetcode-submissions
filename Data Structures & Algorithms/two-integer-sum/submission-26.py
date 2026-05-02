class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for o in range(len(nums)):
            for i in range(o+1, len(nums)):
                if nums[o] + nums[i] == target:
                    return [o,i]