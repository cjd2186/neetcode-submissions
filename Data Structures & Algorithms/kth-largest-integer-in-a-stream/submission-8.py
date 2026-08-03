#max heap??
#heap is a priority queue
#heap should only be size k since k does not change
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        self.heap = self.heap[-k:]

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        heapq.heapify(self.heap)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

