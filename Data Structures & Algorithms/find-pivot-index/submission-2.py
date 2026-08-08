#Algo
#cant sort --> need index, and elements repeat too
#brute force --> go through array each iteration to check sums O(n**2)

#go through once to find full sum, just subtract from the left on a second pass O(n)
#Time | Space
#O(n) | O(1)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum, rsum = 0, 0
        for num in nums:
            rsum += num

        for pivot, num in enumerate(nums):
            rsum -= num
            if lsum == rsum:
                return pivot
            lsum += num
            pivot +=1

        return -1