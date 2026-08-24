#make a dictionary, sort dictionary, return keys
#can do inplace sort with two pointers
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        outDict = defaultdict(str)
        for i in range(0, len(heights)):
            outDict[heights[i]] = names[i]
        
        return list((dict(sorted(outDict.items())[::-1]).values()))