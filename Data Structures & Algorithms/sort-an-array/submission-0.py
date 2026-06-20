class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(start:int, mid : int, end :int, nums) : 
            left_arr = nums[start : mid+1]
            right_arr = nums[mid+1: end+1]
            
            i = j = 0
            idx = start
            while (i < len(left_arr) and j < len(right_arr)):
                if left_arr[i] <= right_arr[j]:
                    nums[idx] = left_arr[i]
                    idx += 1
                    i += 1
                else : 
                    nums[idx] = right_arr[j]
                    j += 1
                    idx += 1

            # fill the remaining values into the array 
            while (i < len(left_arr)):
                nums[idx] = left_arr[i]
                i += 1
                idx += 1

            while (j < len(right_arr)):
                nums[idx] = right_arr[j]
                j += 1 
                idx += 1
             

        def split(start : int ,end : int, nums: List[int] ) :
            if (start < end):
                mid = (start + end) // 2 
                split(start,mid,nums)
                split(mid+1,end,nums)
                merge(start,mid,end,nums)

        length = len(nums) - 1
        split(0,length,nums)

        return nums