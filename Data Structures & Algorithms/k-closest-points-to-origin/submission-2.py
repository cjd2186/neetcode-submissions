class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #dont need to get square root -- uniform operation across all points, just need min
        maxHeap = []
        #need K smallest distances to origin -- y1,y2 is 0,0
        for point in points:
            distance = point[0]**2 + point[1]**2
            #use negative distance, because we want to remove the max distance points
            heapq.heappush(maxHeap, (-distance, point))
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        output = []
        for i in range(k):
            output.append(heapq.heappop(maxHeap)[1])
        
        return output