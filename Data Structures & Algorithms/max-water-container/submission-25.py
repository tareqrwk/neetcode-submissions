class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximum = 0 
        while left < right:
            area = (right - left) * min(heights[right], heights[left])
            maximum = max(area, maximum)
            if heights[left] < heights[right]:
                left += 1
                continue
            right -= 1
        return maximum
                
        