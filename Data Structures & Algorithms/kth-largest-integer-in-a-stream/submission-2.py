class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        print(self.nums)

        i = len(self.nums) - 1
        j = self.k
        while j > 0:
            i -= 1
            j -= 1
        return self.nums[i+1]