#want most 0s to left and most 1s to right as possible
#get sum of the array

#brute force
#time: O(n*2) --> going through left and right at all times
#space: O(n) --> storing each element of array
class Solution:
    def maxScore(self, s: str) -> int:
        maxSplit = 0
        for i in range(len(s)):
            left = s[0:i]
            if not left:
                continue
            right = s[i:]
            left = len(left) - sum([int(num) for num in left])
            right = sum([int(num) for num in right])
            maxSplit = max(maxSplit, left + right)
        return maxSplit