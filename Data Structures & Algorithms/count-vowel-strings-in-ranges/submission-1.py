class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_arr = []
        prefix_sum_arr = []
        ans  = []

        for i in range(len(words)) : 
            word = words[i]
            vowel = "aeiou"
            if word[0] in vowel and word[-1] in vowel:
                vowel_arr.append(1)
            else : 
                vowel_arr.append(0)
            
        # calc prefix_sum 
        prefix_sum_arr.append(vowel_arr[0])
        for i in range(1, len(vowel_arr)):
            prefix_sum_arr.append(prefix_sum_arr[i-1] + vowel_arr[i])
        
        # find the range sum 

        for left,right in queries : 
            if left == 0 : 
                ans.append(prefix_sum_arr[right])
                continue 
            ans.append(prefix_sum_arr[right] - prefix_sum_arr[left-1])

        return ans

        