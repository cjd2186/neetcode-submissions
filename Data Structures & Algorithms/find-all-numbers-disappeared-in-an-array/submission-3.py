#Algo, sort, then remove dupes and have counter, if counter not in arr, add to output
#remove dupes instead of set to ensure to extra space

#sort --> O(n log n) --> can use a dictionary instead?
#for O(n) and no extra space would have to just go through the list once

#one pass --> make output have indexes as values
#second pass --> replace discovered indexes with 0
#third pass --> remove all 0s, left with output
#3*O(n) --> O(n) time
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(1, len(nums) + 1):
            output.append(i)

        for num in nums:
            output[num-1] = 0

        #start index, stop one before end
        for i in range(len(output)-1, -1, -1):
            if output[i] == 0:
                output.pop(i)
        return output