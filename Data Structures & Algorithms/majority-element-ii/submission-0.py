class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq_count = defaultdict(int)
        ans = []

        for num in nums : 
            freq_count[num] += 1
        
        for key,value in freq_count.items(): 
            if value > (len(nums)/3):
                ans.append(key)

        return ans