class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # brute force solution  time complexity -> O(n^2)
                            #   space complexity -> O(1)

        # for i in range(len(nums)-1):
        #     sum = nums[i]
        #     for j in range(i+1,len(nums)):
        #         sum = sum + nums[j]
        #         if sum % k == 0  :
        #             return True 

        # return False

    # Better solution 

        prefix_sum_remainder = defaultdict(int)
        prefix_sum_remainder[0] = -1
        current_sum = 0

        for i,num in enumerate(nums):
            current_sum += num 
            remainder = current_sum % k 
            if remainder in prefix_sum_remainder : 
                if i - prefix_sum_remainder[remainder] >= 2 : 
                    return True
            if remainder not in prefix_sum_remainder :    
                prefix_sum_remainder[remainder]  = i
            
        return False
        





