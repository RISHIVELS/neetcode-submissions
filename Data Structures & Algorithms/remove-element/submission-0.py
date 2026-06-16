class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = []
        for num in nums : 
            if num != val : 
                arr.append(num)
            
        for i in range(len(arr)):
            nums[i] = arr[i]
        
        return len(arr)