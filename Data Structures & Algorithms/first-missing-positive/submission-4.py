class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # num_arr = set()

        # for num in nums : 
        #     num_arr.add(num)

        # for i in range(1,len(num_arr)+1):
        #     if i not in num_arr : 
        #         return i 
        # return len(num_arr) + 1

        # # time complexity ->  O(n)
        # # space complexity -> O(n)

        # optimal solution 

        # clean the array 
        n = len(nums)
        for i in range(n) :
            if nums[i] > n or nums[i] <= 0 :
                nums[i] = n + 1
            
        # swap the number in its curren position
        for i in range(n):
            val = abs(nums[i])
            if val <= n:
                nums[val - 1] = -abs(nums[val - 1])
        
        # check the first missing positive number

        for i in range(n) : 
            if nums[i] > 0 : 
                return i + 1

        return n + 1 




        
        
