class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        highest = float('-inf') 

        arr = sorted(zip(position,speed),key=lambda x : x[0],reverse=True)
        
        for pos, sp in arr : 
            time = (target-pos) / sp 
            if time > highest : 
                highest = time 
                fleet += 1
            
        return fleet