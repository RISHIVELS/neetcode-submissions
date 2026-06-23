class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force approach time complexity -> O(n^2)
        # space complexity -> O(1)
        # _max = 0

        # for i in range(len(heights)):
        #     for j in range(1,len(heights)):
        #         distance = j - i
        #         min_height = min(heights[i],heights[j])
        #         curr = distance * min_height
        #         if curr > _max : 
        #             _max = curr 
        
        # return _max

        # optimised solution 

        _max = 0
        left = 0
        right = len(heights) - 1
        while (left < right):
            distance = right - left 
            min_height = min(heights[left],heights[right])
            capacity = distance * min_height
            if capacity > _max : 
                _max = capacity 
            if heights[left] < heights[right]:
                left += 1
            else : 
                right -= 1
        return _max

        # time complexity -> O(n)
        #  space complexity -> O(1)


