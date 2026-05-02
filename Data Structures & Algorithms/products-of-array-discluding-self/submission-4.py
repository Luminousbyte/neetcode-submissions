class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        
        for i in nums:
            if i == 0:
                zero_count += 1
            else:
                prod *= i
        
        lst = []
        
        for j in nums:
            if zero_count > 1:
                lst.append(0)
            elif zero_count == 1:
                if j == 0:
                    lst.append(prod)
                else:
                    lst.append(0)
            else:
                lst.append(prod // j)
                
        return lst