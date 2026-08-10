#Notes
##a appears twice
##b is missing 
#should have 1, n**2 values in the array
#return [a,b]

#Algo
#naive --> use hashmap/extra array
#in place --> usually use some negatives to mark items
#can use negatives to find repeated values
#can use mod to help access the other levels of the array?

#i.e 7 in a 3*3 array --> 7 - 3 = 4 - 3 = 1 --> two 3s, so [1] of [2] array
#avoid entire retrieval issue by flattening out the array

#find repeated value --> if value is positive, it is repeated
#find missing value --> if index has a positive value, that index is missing

#Time O(m) --> go through array once m is number of elements in grid m = n**2
#Space O(1) --> no extra space used!
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        for i, arr in enumerate(grid):
            if i>0:
                grid[0].extend(arr)
        for num in grid[0]:
            if grid[0][abs(num)-1] > 0:
                grid[0][abs(num)-1] = -1*grid[0][abs(num)-1]
        output = [-1, -1]
        for i,num in enumerate(grid[0]):
            if num > 0:
                output[0] = num
                output[1] = i + 1
        return output
