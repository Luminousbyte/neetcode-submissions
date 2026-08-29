class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i, j = 0, len(heights)-1
        while i<j:
            if heights[i] <= heights[j]:
                wat = heights[i] * (j-i)
                i += 1
                max_water = max(wat, max_water)
            else:
                wat = heights[j] * (j-i)
                j -= 1
                max_water = max(wat, max_water)
        return max_water