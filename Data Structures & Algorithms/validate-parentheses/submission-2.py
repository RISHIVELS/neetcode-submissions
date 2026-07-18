class Solution:
    def isValid(self, s: str) -> bool:
        hash_table = {
            "]":'[',
            "}":'{',
            ")":"("
        }
        l = []
        for i,char in enumerate(s) : 
            if char == "[" or char == "(" or char == "{":
                l.append(char) 
            
            elif  len(l) == 0  or ( l.pop() != hash_table[char]) :
                return False 
        if len(l) == 0 : 
            return True 
        return False 
         
