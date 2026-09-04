from collections import Counter , defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs : 
            key = tuple(sorted(Counter(word).items()))
            group[key].append(word)
        return list(group.values())



                




