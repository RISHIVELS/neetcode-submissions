class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)
        for i, num in enumerate(nums) : 
            compliment = target - num 
            if num in hash_map : 
                return [hash_map[num],i]
            else : 
                hash_map[compliment] = i 
        return False 