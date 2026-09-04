class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_map = {}
        for i in range(len(nums)):
            h_map[nums[i]] = []
        for i in range(len(nums)):
            h_map[nums[i]].append(i)
        for v in h_map.values():
            if len(v) > 1:
                for i in range(1, len(v)):
                    if v[i] - v[i-1] <= k:
                        return True
        return False
        