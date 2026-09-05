class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        largest = 0 
        
        while left < right : 
            area = (right - left) * min(heights[right], heights[left])
            largest = max(area, largest)
            if heights[left] <= heights[right] :
                left += 1
            else : 
                right -= 1
        return largest 




