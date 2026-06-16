from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0 : 
            return 0

        seen = set(nums)
        max_count = 0

        for num in seen : 
            current_num = num
            if current_num - 1 not in seen : 
                count = 1
                while current_num + 1 in seen : 
                    count += 1 
                    current_num += 1
                max_count = max(max_count , count)

        return max_count  

            