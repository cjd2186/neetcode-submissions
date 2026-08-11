class Solution:
    def findLucky(self, arr: List[int]) -> int:
        #use bit manipulation to store frequency with the number
        #max value is 500 --> need 9 bits, 2^9 bits work
        #use 2**10 to push meaningful value to bottom 9 bits
        #anything above is for the counter
        
        for num in arr:
            #lower 9 bits represent the value
            idx_val = num & ((1<<10) - 1)
            if idx_val <= len(arr):
                #increment count at this value
                arr[idx_val-1] += (1<<10)

        #find the num where count == num:
        #value is the value in the original array, not what is being tracked!
        maxOutput = -1
        for i, num in enumerate(arr):
            count = num >> 10
            if count == i + 1:
                maxOutput = max(maxOutput, i+1)
        return maxOutput