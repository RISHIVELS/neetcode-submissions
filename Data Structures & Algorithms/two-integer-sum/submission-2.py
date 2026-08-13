class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in index : 
                return [index[compliment],i]
            index[nums[i]] = i
        return False