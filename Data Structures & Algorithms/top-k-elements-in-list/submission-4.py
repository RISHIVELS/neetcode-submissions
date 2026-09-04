from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for num in nums : 
            hash_map[num] += 1
        
        ans = [num for num, frequence in sorted(hash_map.items(),key= lambda x : x[1],reverse=True)[:k]]
        return ans 