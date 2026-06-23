class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = set()
        
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right :
                sum = nums[left] + nums[right] + nums[i]
                if sum == 0 : 
                    triplet = (nums[left],nums[right],nums[i])
                    curr = tuple(sorted(triplet))
                    ans.add(curr)
                    right -= 1
                elif sum < 0 : 
                    left += 1
                else : 
                    right -= 1
        
        res = [list(s) for s in ans]
        return res