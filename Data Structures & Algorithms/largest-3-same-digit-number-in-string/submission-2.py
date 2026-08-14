#use sliding window to get substrings of length 3!

#Time: O(n) go through nums once
#Space: O(1): only track l, r and array of len 3
class Solution:
    def largestGoodInteger(self, num: str) -> str:

        maxGood = -1
        l = 0
        r = 2
        while r < len(num):
            window = num[l:r+1]
            if (window[0] == window[1]) and (window[1] == window[2]):
                maxGood = max(maxGood, int(window))
            l+=1
            r+=1
        
        if maxGood < 0:
            return ""
        elif maxGood == 0:
            return "000"
        return str(maxGood)