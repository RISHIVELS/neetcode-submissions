class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force solution time complexity -> O(n^2) 
        # space complexity -> O(1)

        # for i in range(k):
        #     last_element = nums.pop()
        #     nums.insert(0,last_element)

        #  Optimised solution 

        left = 0
        rotate = k % len(nums)
        if rotate == 0 : 
            return None

        def num_reverse(left,right,nums):
            l = left 
            r = right
            while (l < r):
                nums[l],nums[r] = nums[r],nums[l]
                l += 1 
                r -= 1

        
        # reverse the array first 
        nums.reverse()
        # reverse first k terms and then the remainig terms
        num_reverse(0,rotate-1,nums)
        num_reverse(rotate,len(nums)-1,nums)

        # time complexity -> O(n)
        # space complexity -> O(1)
        
        
        
        
        

        
