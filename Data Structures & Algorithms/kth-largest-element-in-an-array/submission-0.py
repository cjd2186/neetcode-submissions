class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #kth largest, use minHeap, but pop anything that is outside of the max range
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, -num)
        output = -1001
        for i in range(k):
            output = heapq.heappop(minHeap)
        return -output