class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # edge case
        if len(nums) == 1 : 
            return 1

        unique_arr = []
        for num in nums : 
            if num in unique_arr :
                continue 
            else : 
                unique_arr.append(num)
        
        for i,num in enumerate(unique_arr):
            nums[i] = unique_arr[i]
        
        return len(unique_arr)