class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        longest_prefix = ""
        for char in zip(*strs):
            if len(set(char)) != 1 :
                break
            longest_prefix += char[0]
        return longest_prefix

# time complexity -> O(m.n)
# space complexity -> O(1)