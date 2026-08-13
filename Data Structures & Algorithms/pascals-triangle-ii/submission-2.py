#Edges are always 1 and 1
#can do it recursively?????

#Bottom up dynamic programming
#Use a previously computed result to efficiently compute the next result.
#Time: O(n^2) --> go through row of size up to n n times
#Space: O(n) --> each row made will be of size up to n
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1,1]
        idx = 1
        while idx < rowIndex:
            row = self.recurse(row)
            idx +=1
        return row

    def recurse(self, row) -> List[int]:
        newRow=[1]
        prev = row[0]
        for i in range(1, len(row)):
            curr = row[i]
            newRow.append(prev+curr)
            prev=curr
        newRow.append(1)
        return newRow