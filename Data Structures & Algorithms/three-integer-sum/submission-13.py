class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j<k:
                target = nums[i] + nums[j] + nums[k]
                if target > 0:
                    k -= 1
                elif target < 0:
                    j += 1
                else:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        lst = []
        for i in s:
            lst.append(list(i))
        return lst