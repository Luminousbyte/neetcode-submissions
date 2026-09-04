class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_map = {}
        for i, v in enumerate(nums):
            if v in h_map and i-h_map[v] <= k:
                return True
            h_map[v] = i
        return False