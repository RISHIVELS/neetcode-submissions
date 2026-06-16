from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        max_count = 0

        for num in nums : 
            seen[num] = 1

        for num in nums : 
            current_num = num
            if current_num - 1 in seen : 
                continue 
            count = 1
            while current_num + 1 in seen : 
                count += 1 
                current_num += 1
            max_count = max(max_count , count)

        return max_count  

            