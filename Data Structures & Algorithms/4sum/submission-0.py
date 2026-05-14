class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lst = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            lst.append([nums[i], nums[j], nums[k], nums[l]])
        for i in lst:
            i.sort()

        lst2 = []
        for i in lst:
            if i in lst2:
                continue
            lst2.append(i)
        
        return lst2