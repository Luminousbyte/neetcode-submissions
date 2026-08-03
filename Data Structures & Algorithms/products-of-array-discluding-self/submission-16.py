class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = []
        for n in range(len(nums)):
            lst.append(math.prod(nums[:n]) * math.prod(nums[n+1:]))
        return  lst