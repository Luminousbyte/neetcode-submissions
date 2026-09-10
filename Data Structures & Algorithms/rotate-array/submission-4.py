class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)
        if k < j:
            i = j - k
        if k > j:
            i = j - k%j

        while i:
            num = nums.pop(0)
            nums.append(num)
            i -= 1