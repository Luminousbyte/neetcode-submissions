class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1

        for i in hashmap.items():
            if i[1] > len(nums)//2:
                return i[0]