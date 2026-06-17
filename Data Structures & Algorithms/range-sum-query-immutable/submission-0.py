class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sums = self.calc_prefix_sum()

    def calc_prefix_sum (self):
        prefix_sums = []
        prefix_sums.append(self.nums[0])
        for i in range(1, len(self.nums)):
            prefix_sums.append(prefix_sums[i-1] + self.nums[i])
            
        return prefix_sums    

    def sumRange(self, left: int, right: int) -> int:

        if left == 0 : 
            return self.prefix_sums[right]
        
        return self.prefix_sums[right] - self.prefix_sums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)