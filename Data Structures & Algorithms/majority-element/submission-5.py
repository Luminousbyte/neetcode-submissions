class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        hashmap = defaultdict(int)
        for i in range(l):
            hashmap[nums[i]] += 1

        for k, v in hashmap.items():
            if v > l/2:
                return k