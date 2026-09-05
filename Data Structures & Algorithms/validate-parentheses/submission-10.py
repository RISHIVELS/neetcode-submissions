class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []
        for char in s : 
            if char == "{" or char == "[" or char == "(":
                stack.append(char)
                continue 
            if len(stack) == 0 or stack.pop() != hash_map[char]:  # } == {
                return False 

        if len(stack) != 0 : 
            return False
        return True 