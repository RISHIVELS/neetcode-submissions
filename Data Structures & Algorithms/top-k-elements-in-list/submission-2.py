from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums : 
            return []

        frequent_nums = []
        freq_count = defaultdict(int)

        for num in nums : 
            freq_count[num] += 1 
        
        sorted_freq_count = dict(sorted(freq_count.items(),key = lambda x : x[1],reverse=True))

        for key in sorted_freq_count.keys(): 
            frequent_nums.append(key)

        return frequent_nums[:k]