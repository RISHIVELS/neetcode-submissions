class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # freq_count = defaultdict(int)
        # ans = []

        # for num in nums : 
        #     freq_count[num] += 1
        
        # for key,value in freq_count.items(): 
        #     if value > (len(nums)/3):
        #         ans.append(key)

        # return ans

        majority_ele_1 = 0
        voting_ele_1 = 0

        majority_ele_2 = 0
        voting_ele_2 = 0

        for num in nums : 
            if voting_ele_1 == 0 and num != majority_ele_2 : 
                majority_ele_1 = num 
                voting_ele_1 += 1
            elif voting_ele_2 == 0 and num != majority_ele_1 : 
                majority_ele_2 = num 
                voting_ele_2 += 1
            elif majority_ele_1 == num : 
                voting_ele_1 += 1 
            elif majority_ele_2 == num : 
                voting_ele_2 += 1
            else : 
                voting_ele_1 -= 1 
                voting_ele_2 -= 1
        
        count_ele_1 = 0 
        count_ele_2 = 0 

        for num in nums : 
            if num == majority_ele_1 : 
                count_ele_1 += 1 
            elif num == majority_ele_2 : 
                count_ele_2 += 1
        
        ans = []
        if count_ele_1 > (len(nums)/3):
            ans.append(majority_ele_1)
        if count_ele_2 > (len(nums)/3):
            ans.append(majority_ele_2)
        
        return ans
    
    # time complexity -> O(n)
    # space complexity -> O(1)



