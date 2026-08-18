# sort back and front is nlogn
# remove letters

# have count of all letters
# longest palindrone has even number of each letter except 1
#take half of all evens plus max of odds and all odds without oddMax

#Time: O(n) go through nums linearly
#Space: O(52): upper/lowercase letters so O(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)
        for letter in s:
            if counts[letter] == None:
                counts[letter] = 0
            counts[letter]+=1
        oddMax = 0
        evens=0
        odds=0
        for count in counts.values():
            if count%2==0:
                evens+=count
            else:
                odds+=count-1
                oddMax=max(oddMax,count)
        if odds:
            odds-=oddMax-1
            
        #also add odd counts
        return oddMax + odds + evens

        