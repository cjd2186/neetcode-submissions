#Algo, sort, then remove dupes and have counter, if counter not in arr, add to output
#remove dupes instead of set to ensure to extra space

#sort --> O(n log n) --> can use a dictionary instead?
#for O(n) and no extra space would have to just go through the list once

#assume all numbers are in the output, remove numbers as they appear
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(1,len(nums)+1):
            output.append(i)
        for num in nums:
            if num in output:
                output.remove(num)
        return output