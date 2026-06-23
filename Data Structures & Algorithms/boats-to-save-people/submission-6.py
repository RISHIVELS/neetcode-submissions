class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # edge case
        if len(people) == 1 and people[0] <= limit : 
            return 1

        people.sort()

        left = 0
        right = len(people) - 1
        res = 0

        while left < right:
            _sum = people[left] + people[right]
            if _sum == limit:
                res += 1
                left += 1
                right -= 1
            elif _sum > limit : 
                res += 1
                right -= 1
            else : 
                res += 1 
                left += 1
                right -= 1
        if left == right :
            res += 1


        return res 

        # time complexity -> O(n)
        # space complexity -> O(1)

