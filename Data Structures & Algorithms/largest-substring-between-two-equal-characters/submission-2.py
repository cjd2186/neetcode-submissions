#Algo
# two pointers --> start search, keep searching until next letter
# non optimal since would keep resetting right point --> O(n^2)

# two pointers but start at outside, will automatically be max
#maybe have a hashtable of each char and its separation 

#only 300 total letters, checking 26 isnt horrible
#maybe go through all chars with freq >= 2, go outside in?
#

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        charCount = Counter(s)
        maxLen = -1
        
        print(charCount)
        for char, count in charCount.items():
            l , r = 0, len(s) -1
            if charCount[char] < 2:
                continue
            i = 0
            while l < r:
                if s[l] != char:
                    l +=1
                    continue
                elif s[r] != char:
                    r -=1
                    continue
                #want to break after reached the max
                if s[l] == s[r]:
                    maxLen = max(maxLen, r - l - 1)
                    break
        return maxLen