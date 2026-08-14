#sort both strings, should be the same
#Time: O(nlogn) to sort
#Space: O(n), create new objects
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(list(s)) == sorted(list(t)):
            return True
        else:
            return False