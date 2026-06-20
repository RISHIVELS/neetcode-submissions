class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force solution 

        arr = [-1]*len(nums)

        left = 0 
        right = -1 

        for num in nums : 
            if num == 0 :
                arr[left] = 0
                left += 1 
            elif num == 2 : 
                arr[right] = 2
                right -= 1

        for i , num in enumerate(arr):
            if num == -1 : 
                nums[i] = 1 
            else : 
                nums[i] = num
                
        