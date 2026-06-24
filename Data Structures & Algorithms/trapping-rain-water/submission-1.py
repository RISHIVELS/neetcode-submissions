class Solution:
    def trap(self,height: List[int]) -> int:
        if len(height) == 1 : 
            return 0

        left = 1
        right  = len(height) - 2
        res = 0

        def find_left_largest(left):
            left_high = 0
            while (left>=0):
                left_high = max(left_high,height[left])
                left -= 1
            return left_high
        
        def find_right_largest(right):
            right_high = 0
            while right < len(height):
                right_high = max(right_high,height[right])
                right += 1
            return right_high

        for i in range(1,len(height)-1):
            left = find_left_largest(i-1)
            right = find_right_largest(i+1)
            water = min(left,right) - height[i]
            if water <= 0 : 
                continue 
            else : 
                res += water
                
        return res
                



