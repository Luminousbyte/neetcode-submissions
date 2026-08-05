class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        for i in range(len(nums)):
            p, q = i+1, len(nums)-1
            while p<q:
                if nums[p] + nums[q] + nums[i] > 0:
                    q -= 1
                elif nums[p] + nums[q] + nums[i] < 0:
                    p += 1
                else:
                    s.add((nums[i], nums[p], nums[q]))
                    p += 1
                    q -= 1
        lst = []
        for i in s:
            lst.append(list(i))
        
        return lst