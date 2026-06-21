class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort(nums):
            min_num = min(nums)
            max_num = max(nums)
            _range = max_num - min_num + 1
            arr = [0]*_range
            for i , num in enumerate(nums):
                shift = num - min_num
                arr[shift] += 1

            prefix_arr = []
            prefix_arr.append(arr[0])
            for i in range(1,len(arr)) :
                prefix_arr.append(arr[i] + prefix_arr[i-1])

            res = [0]*len(nums)

            for i in range(len(nums)-1,-1,-1):
                shift = nums[i] - min_num
                index = prefix_arr[shift] - 1
                res[index] = nums[i]
                prefix_arr[shift] -= 1

            return res 
        
        res = counting_sort(nums)
        return res