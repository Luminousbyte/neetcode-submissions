class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for idx, val in enumerate(nums):
            lst.append([val, idx])
        lst.sort()

        i, j = 0, len(lst)-1

        while i<j:
            if lst[i][0] + lst[j][0] < target:
                i += 1
            elif lst[i][0] + lst[j][0] > target:
                j -= 1
            else:
                return sorted([lst[i][1], lst[j][1]])
        return [-1]    