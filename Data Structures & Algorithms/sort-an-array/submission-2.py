import random
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def quick_sort(low,high,nums) ->int: 
            pivot_index = random.randint(low,high)
            nums[low],nums[pivot_index] = nums[pivot_index],nums[low]
            pivot = nums[low]
            i = low
            j = high

            while (i < j):
                # find the element greater than pivot in the left half
                while  nums[i] <= pivot and i <= high-1  :
                    i += 1
                # find the element smaller than the pivot in the right half 
                while  nums[j] > pivot and j >= low+1   : 
                    j -= 1
                # check if the i and j are not crossed if so swap the elements
                if i < j : 
                    nums[i],nums[j] = nums[j], nums[i]
                # swap the jth and lowth position values at last 
            nums[low],nums[j] = nums[j], nums[low]
            return j

        def sort(low,high,nums):
            if (low < high):
                pivot = quick_sort(low,high,nums)
                sort(low,pivot-1,nums)
                sort(pivot+1,high,nums)

        low = 0
        high = len(nums) - 1
        sort(low,high,nums)

        return nums

