class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_1 = [-i for i in nums]
        heapq.heapify(nums_1)
        
        while k>1:
            heapq.heappop(nums_1)
            k -= 1
        return -nums_1[0]
            