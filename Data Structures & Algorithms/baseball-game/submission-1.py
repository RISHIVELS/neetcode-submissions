class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for op in operations :
            if op.lstrip("-").isnumeric() : 
                print(op)
                l.append(int(op))
            
            elif op == "+":
                n = len(l)
                value = l[n-1] + l[n-2]
                l.append(value)
            
            elif op == "D":
                value = l[-1]* 2
                l.append(value)
            
            else : 
                l.pop()
        
        return sum(l)
        # 5 -2 -4 9 5 14 = 
        # time complexity ->  O(n)
        # space complexity -> O(n)