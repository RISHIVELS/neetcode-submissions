from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use hashmap for this 

        hash_map_1 = defaultdict(int)
        for string in s : 
            hash_map_1[string] += 1
        
        for string in t : 
            if hash_map_1[string] == 0 : 
                return False 
            else : 
                hash_map_1[string] -= 1
        
        for string, num in hash_map_1.items():
            if num > 0 : 
                return False 
        return True 

        