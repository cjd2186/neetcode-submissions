#sort both strings, should be the same
#O(nlogn) to sort, sort inplace
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(list(s)) == sorted(list(t)):
            return True
        else:
            return False