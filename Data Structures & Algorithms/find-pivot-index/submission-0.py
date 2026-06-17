class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum_array = []
        prefix_sum_array.append(nums[0])

        for i in range(1,len(nums)):
            prefix_sum_array.append(prefix_sum_array[i-1] + nums[i])

        for i in range(len(nums)):
            if i == 0 : 
                left_sum = 0
            else : 
                left_sum = prefix_sum_array[i-1]
            right_sum = prefix_sum_array[-1] - prefix_sum_array[i]

            if left_sum == right_sum : 
                return i 

        return -1