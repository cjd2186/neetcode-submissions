#Use counters

#Time: O(n))
#Space: O(n), creating counters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = Counter(s)
        tCount = Counter(t)
        return tCount == sCount