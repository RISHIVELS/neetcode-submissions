class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force approach 

        product_nums = []

        for i in range(len(nums)):
            current_product = 1
            for j in range(len(nums)):
                if i==j : 
                    continue 
                current_product = current_product * nums[j]
            
            product_nums.append(current_product)
        
        return product_nums