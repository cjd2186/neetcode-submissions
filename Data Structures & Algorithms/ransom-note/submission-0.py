#Time: O(n)
#Space: O(1) -- 26 letters mask

#frequency of ransomNote must be less than or equal to frequency of magazine
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomFreq = Counter(ransomNote)
        magFreq = Counter(magazine)
        
        for key in ransomFreq:
            if ransomFreq[key] > magFreq[key]:
                return False

        return True