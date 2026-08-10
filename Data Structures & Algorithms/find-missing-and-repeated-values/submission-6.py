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

#Time O(n**2) --> go through array once, number of elements in grid is n**2
#Space O(n**2) --> extra space, can be reduced by just modifying the array instead of flattening it
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        repeated = -1
        missing = -1
        #just modify values in place
        for i in range(n):
            for j in range(n):
                num = abs(grid[i][j])
                index = num - 1
                row = index // n
                col = index % n
                if grid[row][col]> 0:
                    grid[row][col] = -1*abs(grid[row][col])
                else:
                    repeated = num
        #Find index that wasnt marked as negative
        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                if num > 0:
                    missing = i * n + j + 1
        return [repeated, missing]