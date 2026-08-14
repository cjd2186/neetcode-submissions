#sort both strings, should be the same
#Time: O(nlogn) to sort
#Space: O(n), create new lists
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))