class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        area = 0

        while left < right:
            currArea = (right - left) * min(heights[left],heights[right])
            area = max(area,currArea)
            
            if heights[left]<heights[right]:
                left += 1
            else:
                right -=1
        
        return area

        