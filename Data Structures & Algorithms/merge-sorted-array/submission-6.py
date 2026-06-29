class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = [0]*(m+n)
        left = 0 
        right  = 0
        index = 0
        while left < m and right < n : 
            if nums1[left] <= nums2[right]:
                res[index] = nums1[left]
                index += 1
                left += 1
            else  : 
                res[index] = nums2[right]
                index += 1 
                right += 1
        while left < m : 
            res[index] = nums1[left]
            index += 1
            left += 1
        while right < n : 
            res[index] = nums2[right]
            index += 1
            right += 1

        for i in range(len(res)):
            nums1[i] = res[i]

    # #  time complexity -> O(m+n)
    # #  space complexity -> O(m+n)



