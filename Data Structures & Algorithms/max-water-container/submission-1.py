class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area_lst = []
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j-i
                
                area = min(heights[i], heights[j]) * width
                area_lst.append(area)
                
        return max(area_lst)