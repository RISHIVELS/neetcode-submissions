class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        for token in tokens : 
            if token.lstrip("-").isnumeric() :
                stack.append(int(token))
            else : 
                num1 = stack.pop()
                num2 = stack.pop()
                result = 0
                if token == '+':
                    result = num2 + num1 
                elif token == "-" :
                    result = num2 - num1
                elif token == "*" :
                    result = num2 * num1 
                else : 
                    result = int(num2/num1)
                stack.append(result)
        return stack.pop()