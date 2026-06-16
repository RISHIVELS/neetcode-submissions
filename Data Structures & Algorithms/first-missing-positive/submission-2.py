class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_arr = set()
        missing_num = float('inf')

        for num in nums : 
            num_arr.add(num)

        for i in range(1,len(num_arr)+1):
            if i not in num_arr : 
                return i 
        return len(num_arr) + 1



        
        
