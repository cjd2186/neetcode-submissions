#Bit mask
#use a number for each string 
#bit mask, first 26 bits correspond to letters
#ascii values to get mapping of chars to bits

#ord(x) - ord('a') --> character minus 55 to get the smaller mapping
#bitwise OR to set the bit, shift to the left by the value times

#compare bitmask with the allowed bitmask using bitwise & (are these two the same)
#Time: O(w) where w is the number of total letters in words
#Space: O(1) --> bitmask 26 bits
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        bitmask = 0
        for char in allowed:
            #shift left the number of times based on the bit
            bit = 1 << (ord(char) - ord('a'))
            #want to add but to mitmask with or
            bitmask = bitmask | bit

        res = len(words)
        for word in words:
            wordMask = 0
            for char in word:
                bit = 1 << (ord(char) - ord('a'))
                #check if bit is in the bitmask
                if bit & bitmask == 0:
                    res -= 1
                    break
        return res