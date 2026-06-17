class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        max_count = 0

        for num in s : 
            if num=="1":
                right += 1
        
        for i in range(len(s)-1) : 
            if s[i] == "0":
                left += 1 
                max_count = max(max_count, left+right)
            else : 
                right -= 1
                max_count = max(max_count, left+right)

        return max_count
