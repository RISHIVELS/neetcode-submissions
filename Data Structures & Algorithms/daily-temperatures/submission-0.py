class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use next greater element pattern -> stack 
        ans = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)-1,-1,-1):
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if len(stack) == 0 : 
                ans[i] = 0
            else : 
                ans[i] = stack[-1] - i
            stack.append(i)
        
        return ans 