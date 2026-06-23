class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4 : 
            return []
        nums.sort()
        ans = set()
        
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j + 1 
                right = len(nums) - 1
                while (left < right):
                    _sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if _sum == target : 
                        triplet = (nums[i],nums[j],nums[left],nums[right])  
                        curr = tuple(sorted(triplet))
                        ans.add(curr)
                        right -= 1
                    elif _sum > target : 
                        right -= 1
                    else : 
                        left += 1 
        ans = [list(s) for s in ans]
        return ans