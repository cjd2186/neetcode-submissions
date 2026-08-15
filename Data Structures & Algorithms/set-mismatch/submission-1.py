class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #numbers are from 1 to n
        counts = defaultdict(int)
        for i in range(1, len(nums)+1):
            counts[i] = 0
        for num in nums:
            counts[num] +=1
        a = -1
        b = -1
        for key, val in counts.items():
            if val == 0:
                b = key
            if val == 2:
                a = key
        return [a,b]