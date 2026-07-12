class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
    #     res = [0]*(m+n)
    #     left = 0 
    #     right  = 0
    #     index = 0
    #     while left < m and right < n : 
    #         if nums1[left] <= nums2[right]:
    #             res[index] = nums1[left]
    #             index += 1
    #             left += 1
    #         else  : 
    #             res[index] = nums2[right]
    #             index += 1 
    #             right += 1
    #     while left < m : 
    #         res[index] = nums1[left]
    #         index += 1
    #         left += 1
    #     while right < n : 
    #         res[index] = nums2[right]
    #         index += 1
    #         right += 1

    #     for i in range(len(res)):
    #         nums1[i] = res[i]

    # #  time complexity -> O(m+n)
    # #  space complexity -> O(m+n)

        length = m + n - 1
        p1 = m - 1 
        p2 = n - 1

        while p1 >= 0 and p2 >= 0  : 
            if nums1[p1] > nums2[p2]:
                nums1[length] = nums1[p1]
                p1 -= 1
                length -= 1
            else : 
                nums1[length] = nums2[p2]
                p2 -= 1
                length -= 1
        while p1 >= 0 and length >= 0:
            nums1[length] = nums1[p1]
            length -= 1 
            p1 -= 1
        while p2 >= 0 and length >= 0 : 
            nums1[length] = nums2[p2]
            length -= 1 
            p2 -= 1



