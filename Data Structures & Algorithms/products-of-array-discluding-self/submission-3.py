class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [0]*len(nums)
        right_arr = [0]*len(nums)
        left_arr[0] = 1
        right_arr[len(nums)-1] = 1 
        # left array 
        for i in range(1, len(nums)):
            left_arr[i] = nums[i-1] * left_arr[i-1]
        # right array 
        for j in range(len(nums)-2,-1,-1):
            right_arr[j] = right_arr[j+1] * nums[j+1]
        
        ans = []
        for i in range(len(nums)):
            ans.append(left_arr[i] * right_arr[i])
        
        return ans 
