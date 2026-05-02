class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = []
        for idx, num in enumerate(nums):
            nums_set.append([num, idx])
        
        nums_set.sort()
        l, r = 0, len(nums) - 1
        while l<r:
            sum = nums_set[l][0] + nums_set[r][0]
            if sum == target:
                return [min(nums_set[l][1], nums_set[r][1]), max(nums_set[l][1], nums_set[r][1])]
            elif sum > target:
                r -= 1
            else:
                l += 1
        return []