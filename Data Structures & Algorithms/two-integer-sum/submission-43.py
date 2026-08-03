class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for idx, num in enumerate(nums):
            lst.append([num, idx])
        lst.sort()
        i, j = 0, len(nums)-1
        while i<j:
            if lst[i][0] + lst[j][0] > target:
                j -= 1
            elif lst[i][0] + lst[j][0] < target:
                i += 1
            else:
                return sorted([lst[i][1], lst[j][1]])