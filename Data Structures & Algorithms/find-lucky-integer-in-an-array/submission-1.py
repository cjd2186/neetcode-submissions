class Solution:
    def findLucky(self, arr: List[int]) -> int:
        #O(n) time, O(n) space
        count = Counter(arr)
        maxOutput = -1
        for key, val in count.items():
            if key == val:
                maxOutput = max(maxOutput, key)
        return maxOutput