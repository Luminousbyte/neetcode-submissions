class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_set = set()
        l = 0

        for r in range(len(nums)):
            if r-l > k:
                h_set.remove(nums[l])
                l += 1
            if nums[r] in h_set:
                return True
            h_set.add(nums[r])
        return False