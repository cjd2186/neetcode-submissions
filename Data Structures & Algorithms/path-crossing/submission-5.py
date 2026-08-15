#Algo
#can keep track of all points traversed, if current point is in traversed, paths cross

#Time: O(n) --> one pass, but search each element of pathes using set for O(1) lookup
#Space: O(n)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pathes = set()
        curr=(0,0)
        pathes.add(curr)
        for move in path:
            curr = list(curr)
            if move ==   'N':
                curr[0] +=1
            elif move == 'S':
                curr[0] -=1
            elif move == 'E':
                curr[1] +=1
            elif move == 'W':
                curr[1] -=1
            if tuple(curr) in pathes:
                return True
            pathes.add(tuple(curr.copy()))
        return False