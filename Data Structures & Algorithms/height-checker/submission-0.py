#sort --> nlogn
#O(n) --> go through heights in one pass
#use min/max?
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        inc = 0
        ceiling = heights[0]
        nonDesc = sorted(heights)
        for i, height in enumerate(heights):
            if nonDesc[i] != height:
                inc+=1
        return inc