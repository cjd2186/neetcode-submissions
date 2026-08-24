#Algo 
#   any sort is at least nlogn

#each eleemtn in arr2 is in arr1!
#make output, arr2, then just do a lookup as a dictionary
#merge all of the values into an output array

#O(n) time, O(n) space
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        outDict = defaultdict(list)
        for num in arr2:
            outDict[num]= []
        
        output = []
        for num in arr1:
            if num not in outDict.keys():
                output.append(num)
            else:
                outDict[num].append(num)
        
        #O(n)?
        output.sort()
        dictoutput = []
        for key,val in outDict.items():
            dictoutput.extend(val)
        
        dictoutput.extend(output)
        return dictoutput