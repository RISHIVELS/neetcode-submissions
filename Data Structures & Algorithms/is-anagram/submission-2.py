from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        for letter in s : 
            freq[letter] += 1
        for letter in t : 
            if letter not in freq : 
                return False
            freq[letter] -= 1 
        for value in freq.values():
            if value > 0 : 
                return False 
        return True
