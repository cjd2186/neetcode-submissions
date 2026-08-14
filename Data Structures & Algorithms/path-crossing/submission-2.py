#Algo
#can keep track of all points traversed, if current point is in traversed, paths cross
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pathes = [[0,0]]
        curr=[0,0]
        for move in path:
            if move == 'N':
                curr[0] +=1
            elif move =='S':
                curr[0] -=1
            elif move == 'E':
                curr[1] +=1
            elif move == 'W':
                curr[1] -=1
            if curr in pathes:
                return True
            pathes.append(curr.copy())
        return False