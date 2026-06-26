class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.findPossibleWays(nums, 0, 0, target)

    def findPossibleWays(self, arr, i, s, target):

        # If target is reached, return 1
        if s == target and i == len(arr):
            return 1

        # If all elements are processed and
        # target is not reached, return 0
        if i >= len(arr):
            return 0

        # Return total count of two cases
        # 1. Add current element
        # 2. Subtract current element
        return (self.findPossibleWays(arr, i + 1, s + arr[i], target) +
                self.findPossibleWays(arr, i + 1, s - arr[i], target))