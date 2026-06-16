from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # edge cases
        # if the list lenght is one 
        if len(strs) == 1 : 
            return [[strs[0]]]
        
        repetetion_tracker = []
        same_word_index = {}

        for i in range(len(strs)):
            if i in repetetion_tracker : 
                continue 
            current_word = strs[i]
            current_word_freq = Counter(current_word)
            repetetion_tracker.append(i)
            same_word_index[strs[i]] = [i]

            for j in range(i+1,len(strs)):
                next_word_freq = Counter(strs[j])
                if current_word_freq == next_word_freq : 
                    same_word_index[strs[i]].append(j)
                    repetetion_tracker.append(j)
        
        anagram = []
        for list_index in same_word_index.values():
            li = []
            for i in list_index : 
                li.append(strs[i])
            anagram.append(li)
        
        return anagram


                




