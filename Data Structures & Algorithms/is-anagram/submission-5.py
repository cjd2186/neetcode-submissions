#Use counters

#Time: O(n))
#Space: O(1), at most 26 chars in Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)
        return tCount == sCount