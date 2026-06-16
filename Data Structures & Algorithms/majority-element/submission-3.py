from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freq = defaultdict(int)

        # for num in nums : 
        #     freq[num]+=1
        #     if freq[num] > (len(nums)/2):
        #         return num 


        # time complexity -> O(n)
        # space complexity -> O(n)

        # moores voting algorithm

        majority = 0
        voting = 0

        for num in nums : 
            if voting == 0 : 
                majority = num 
                voting += 1
            elif majority != num : 
                voting -= 1
            elif majority == num : 
                voting += 1 
        
        return majority












