class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # edge case
        # if len(nums) == 1 : 
        #     return 1

        # unique_arr = []
        # for num in nums : 
        #     if num in unique_arr :
        #         continue 
        #     else : 
        #         unique_arr.append(num)
        
        # for i,num in enumerate(unique_arr):
        #     nums[i] = unique_arr[i]
        
        # return len(unique_arr)
        # time complexity -> O(n)
        # space complexity -> O(n)

        # optimal solution 

        left  = right = 0
        n = len(nums)
        while right < n : 
            nums[left] = nums[right]
            while right < n and nums[left] == nums[right]  : 
                right += 1
            left += 1
        return left 

        # time complexity -> O(n)
        # space complexity -> O(1)


