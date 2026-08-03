class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1*stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x==y:
                continue
            else:
                heapq.heappush(maxHeap, -1*abs(x-y))
        if len(maxHeap) == 1:
            return -1*maxHeap[0]
        else:
            return 0