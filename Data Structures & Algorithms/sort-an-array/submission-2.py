class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i-1
            while temp < nums[j] and j>-1:
                nums[j+1] = nums[j]
                nums[j] = temp
                j -= 1
        return nums