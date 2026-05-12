class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            if i != min_index:
                temp = nums[i]
                nums[i] = nums[min_index]
                nums[min_index] = temp
        return nums