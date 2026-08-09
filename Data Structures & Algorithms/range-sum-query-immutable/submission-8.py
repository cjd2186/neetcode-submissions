#Algo
#total the sum of values before each item in nums -- O(n) to build
# then each call becomes a lookup for the sum instead of a computation -- O(1)

#space is O(n) for prefix tree (unavoidable)
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        total = 0
        for i, num in enumerate(nums):
            total += num
            self.nums[i]=total
    def sumRange(self, left: int, right: int) -> int:
        print(self.nums)
        print(left,right)
        if left -1 < 0:
            left_sum = 0
        else:
            left_sum = self.nums[left-1]
        return self.nums[right] - left_sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)