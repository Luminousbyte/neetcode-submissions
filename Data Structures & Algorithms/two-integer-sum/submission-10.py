class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for ind, num in enumerate(nums):
            lst.append([num, ind])

        lst.sort()
        i, j = 0, len(lst)-1
        while i < j:
            if lst[i][0] + lst[j][0] == target:
                return [min(lst[i][1], lst[j][1]), max(lst[i][1], lst[j][1])]
            elif lst[i][0] + lst[j][0] < target:
                i += 1
            else:
                j -= 1
        return []