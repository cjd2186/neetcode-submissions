#use one integer instead!

#Time: O(n) go through nums once
#Space: O(1): only track one number
class Solution:
    def largestGoodInteger(self, num: str) -> str:

        maxGood = -1

        for i in range(len(num)-2):
            if (num[i] == num[i+1]) and (num[i+1] == num[i+2]):
                maxGood = max(maxGood, int(num[i]))
        
        return "" if maxGood < 0 else 3*str(maxGood)