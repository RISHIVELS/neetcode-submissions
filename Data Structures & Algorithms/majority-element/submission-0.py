from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        current_max_count = 0 
        majority_element = nums[0]

        for num in nums : 
            freq[num]+=1
        
        for key,value in freq.items() : 
            if value > current_max_count :  
                majority_element = key 
                current_max_count = value
        
        return majority_element

        