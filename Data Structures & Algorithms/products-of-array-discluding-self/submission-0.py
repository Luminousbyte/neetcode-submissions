class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = nums.count(0)

        if zero_count == 0:
            for i in nums:
                prod *= i
            lst = [prod//i for i in nums]
        elif zero_count == 1:
            prod = 1
            for i in nums:
                if i!= 0:
                    prod *= i
            lst = [prod if i==0 else 0 for i in nums]
        else:
            lst = [0 for _ in nums]
        return lst