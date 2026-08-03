class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        lst = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                prod *= nums[j]
            lst.append(prod)
            prod = 1
        return lst