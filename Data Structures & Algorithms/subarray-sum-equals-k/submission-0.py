from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialise the hash freq for prefix sum
        prefix_sum_freq = defaultdict(int)
        prefix_sum_freq[0] = 1
        # initialise the variables
        total_subarray = 0
        prefix_sum = 0
        # loop through and check
        for num in nums : 
            prefix_sum += num 
            if (prefix_sum-k in prefix_sum_freq):
                total_subarray += prefix_sum_freq[prefix_sum - k]
            prefix_sum_freq[prefix_sum] += 1 
        
        return total_subarray
