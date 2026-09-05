class Solution:
    def trap(self,height: List[int]) -> int:
        # find the left -> right highest 
        left_arr = [0] * len(height)
        left_arr[0] = height[0]

        for i in range(1, len(height)):
            left_arr[i] = max(height[i],left_arr[i-1])
        
        # find the right -> left highest
        right_arr = [0] * len(height)
        right_arr[-1] = height[-1]
        
        for j in range(len(height)-2,-1,-1):
            right_arr[j] = max(height[j],right_arr[j+1])
        
        total_water = 0
        for i in range(len(height)):
            current_height = height[i]
            value = min(left_arr[i],right_arr[i]) - current_height
            total_water += value 
        return total_water
        