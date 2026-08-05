class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #dont need to get square root -- uniform operation across all points, just need min
        minHeap = []
        #need K smallest distances to origin -- y1,y2 is 0,0
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(minHeap, (-distance, point))
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        output = []
        for i in range(k):
            output.append(heapq.heappop(minHeap)[1])
        
        return output