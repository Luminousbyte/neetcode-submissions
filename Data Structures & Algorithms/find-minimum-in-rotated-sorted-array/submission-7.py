class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def helper(l, r, res):
            # base case
            if l > r:
                return res
            
            # if subarray is already sorted
            if nums[l] < nums[r]:
                return min(res, nums[l])
            
            m = (l + r) // 2
            res = min(res, nums[m])
            
            # left part is sorted
            if nums[m] >= nums[l]:
                return helper(m + 1, r, res)
            else:
                return helper(l, m - 1, res)
        
        return helper(0, len(nums) - 1, nums[0])