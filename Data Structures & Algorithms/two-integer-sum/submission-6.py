class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for ind, num in enumerate(nums):
            A.append([num, ind])

        A.sort()
        left, right = 0, len(nums)-1

        while left<right:
            curr = A[left][0] + A[right][0]
            if curr < target:
                left += 1
            elif curr > target:
                right -= 1
            else:
                return [min(A[left][1], A[right][1]), max(A[left][1],A[right][1])]
        return []