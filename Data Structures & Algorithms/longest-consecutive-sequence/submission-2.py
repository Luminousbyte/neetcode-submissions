class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nu_nums = set(nums)
        max_count = 0
        for num in nums:
            if num - 1 not in nu_nums:
                curr = num
                count = 1
                while curr + 1 in nu_nums:
                    curr += 1
                    count += 1
                max_count = max(count, max_count)
        return max_count