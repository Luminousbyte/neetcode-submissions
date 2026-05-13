class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[j] == nums[i] and abs(j-i) <= k:
                    return True
        return False