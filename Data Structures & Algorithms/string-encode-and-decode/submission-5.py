class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs : 
            res += str(len(word)) + '#'
            res += word 

        return res  


    def decode(self, s: str) -> List[str]:
        ans = []

        left = 0
        while (left < len(s)):
            separator = s.index('#',left)
            num = int(s[left : separator])
            start = separator + 1
            end = start + num
            word = s[start : end]
            ans.append(word)
            left = end 
        return ans 


