class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        i, j = 0, len(heights)-1
        while i<j:
            a = min(heights[i],heights[j]) * (j-i)
            if heights[i]<heights[j]:
                i += 1
            else:
                j -= 1
            max_a = max(a, max_a)
        return max_a