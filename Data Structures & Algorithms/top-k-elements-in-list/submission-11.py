class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = {}
        for num in nums:
            set_nums[num] = 1 + set_nums.get(num, 0)

        lst = []
        for keys, times in set_nums.items():
            lst.append([times, keys])
        lst.sort()

        res = []
        while len(res)<k:
            res.append(lst.pop()[1])
        return res