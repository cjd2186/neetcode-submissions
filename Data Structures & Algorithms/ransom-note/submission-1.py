#Time: O(n)
#Space: O(1) -- 26 letters mask

#frequency of ransomNote must be less than or equal to frequency of magazine
#make a list of 26, each index corresponds to 1 bit
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26
        for letter in magazine:
            count[ord(letter) - ord('a')] +=1
        
        for letter in ransomNote:
            count[ord(letter) - ord('a')] -=1
            if count[ord(letter) - ord('a')] < 0:
                return False
        return True