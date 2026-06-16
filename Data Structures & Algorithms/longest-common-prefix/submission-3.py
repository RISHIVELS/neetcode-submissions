class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):
            current_letter = strs[0][i]
            for other_word in strs[1:]:
                if i==len(other_word) or  other_word[i] != current_letter:
                    return strs[0][:i]
        return strs[0]
