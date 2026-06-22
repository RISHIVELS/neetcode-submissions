class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        left = 0 
        right = 0

        while left < len(word1) and right < len(word2) :
            if left == right : 
                res += word1[left]
                left += 1
            else : 
                res += word2[right]
                right += 1
        while left < len(word1):
            res += word1[left]
            left += 1
        while right < len(word2):
            res += word2[right]
            right += 1
        
        return res 

        # time complexity -> O(m+n)
        # space complexity -> O(1)