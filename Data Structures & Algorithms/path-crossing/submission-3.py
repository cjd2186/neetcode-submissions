#Algo
#can keep track of all points traversed, if current point is in traversed, paths cross

#Time: O(n^2) --> one pass, but search each element of pathes --optimize
#Space: O(n)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pathes = ["00"]
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
            str_curr = str(curr[0]) + str(curr[1])
            pathes.append(str_curr)
        pathCounts = defaultdict(int)
        for path in pathes:
            if pathCounts[path] == None:
                pathCounts[path] = 0
            else:
                pathCounts[path] += 1
        for path in pathCounts.values():
            if path > 1:
                return True
        return False