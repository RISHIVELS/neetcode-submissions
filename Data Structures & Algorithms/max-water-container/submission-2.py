class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force approach 
        _max = 0

        for i in range(len(heights)):
            for j in range(1,len(heights)):
                distance = j - i
                min_height = min(heights[i],heights[j])
                curr = distance * min_height
                if curr > _max : 
                    _max = curr 
        
        return _max
