from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : 
            return 0 

        largest = 1
        hash_set = set(nums)
        for num in nums : 
            if num - 1 in hash_set : 
                continue 
            current = 1
            while num + 1 in hash_set : 
                current += 1
                num += 1
            largest = max(current, largest) 
                
        return largest 
            