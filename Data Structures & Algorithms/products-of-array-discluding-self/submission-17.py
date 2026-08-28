class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        if number of zeroes is more than 1:
            entire list is 0
        if number of zeroes is equal to 1:
            entire list except number 0's index is 0.
        """

        zero_cnt = 0
        for i in nums:
            if i == 0:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return [0]*len(nums)
        elif zero_cnt < 1:
            prod = 1
            lst = []
            for i in nums:
                prod *= i
            for i in nums:
                lst.append(prod//i)
            return lst
        else:
            prod = 1
            idx = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    idx = i
                    continue
                prod *= nums[i]
            lst = [0]*len(nums)
            lst[idx] = prod
            return lst

            