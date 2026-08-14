#more elegant Solution
#I know all the 1s in the array -- sum
#can see how many 1s are to right by subtracting 1 each Time

#how many 0s are to the left? can count it as I go, but 0 at the first 0


#Time 
#Space
class Solution:
    def maxScore(self, s: str) -> int:
        maxSplit = 0
        ones = sum(int(num) for num in s)
        zeroes = 0
        for i in range(0, len(s)-1):
            if s[i] == '1':
                ones -=1
            elif s[i] == '0':
                zeroes+=1
            maxSplit = max(maxSplit, zeroes + ones)        
        return maxSplit
