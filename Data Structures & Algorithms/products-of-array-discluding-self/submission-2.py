class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force approach 

        # product_nums = []

        # for i in range(len(nums)):
        #     current_product = 1
        #     for j in range(len(nums)):
        #         if i==j : 
        #             continue 
        #         current_product = current_product * nums[j]
            
        #     product_nums.append(current_product)
        
        # return product_nums  time complexity -> O(n^2)

        prefix_product = [0]*len(nums)
        suffix_product = [0]*len(nums)
        ans = []
        
        prefix_product[0] = 1
        suffix_product[-1] = 1

        for i in range(1,len(nums)):
            current_value = prefix_product[i-1] * nums[i-1]
            prefix_product[i] = current_value

        for i in range(len(nums)-2,-1,-1):
            current_value = suffix_product[i+1] * nums[i+1]
            suffix_product[i] = current_value
 
        for i in range(len(nums)):
            ans.append(prefix_product[i] * suffix_product[i])

        return ans

