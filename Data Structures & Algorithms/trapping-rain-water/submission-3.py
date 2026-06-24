class Solution:
    def trap(self,height: List[int]) -> int:

        n = len(height)
        if n <= 1 : 
            return 0
        
        n = len(height)
        res = 0
        left = [0]*n
        right = [0]*n
        left[0] = 0
        right[n-1] = 0

        for i in range(1,n):
            left[i] = max(left[i-1],height[i-1])
        for j in range(n-2,-1,-1):
            right[j] = max(right[j+1],height[j+1])
        


        for i in range(1,len(height)-1):
            left_max = left[i]
            right_max = right[i]
            water = min(left_max,right_max) - height[i]
            if water <= 0 : 
                continue 
            else : 
                res += water
                
        return res
                



