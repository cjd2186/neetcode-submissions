#counting sort
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #O(n)
        count = Counter(heights)
        countSort = []
        #O(n+k) --> k being the highest frequency
        #can go from 1 to 100 because range is limited
        for key in range(1, 101):
            value = count[key]
            for val in range(value):
                countSort.append(key)
        inc = 0
        for i, height in enumerate(heights):
            if countSort[i] != height:
                inc+=1
        return inc