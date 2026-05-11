class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for id, val in enumerate(nums):
            lst.append([val, id])
        lst.sort()

        l, r = 0, len(lst)-1
        while l<r:
            if lst[l][0] + lst[r][0] > target:
                r -= 1
            elif lst[l][0] + lst[r][0] < target:
                l += 1
            else:
                return sorted([lst[l][1],lst[r][1]])
        return []