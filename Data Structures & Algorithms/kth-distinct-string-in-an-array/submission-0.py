#Algo
# go through arr, increment value if already seen
# return kth key with value 1
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = defaultdict(str)
        for string in arr:
            if string in distinct.keys():
                distinct[string]+=1
            else:
                distinct[string]=1
        for string, count in distinct.items():
            if count == 1:
                k-=1
            if k==0:
                return string
        return ""