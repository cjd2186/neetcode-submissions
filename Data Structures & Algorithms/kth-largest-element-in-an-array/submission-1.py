class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #kth largest, use maxHeap, but pop anything that is outside of the max range
        #useMax heap --> idea is to add all items to heap
        #keep popping items from heap until you get to the kth largest
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)
        output = -1001
        for i in range(k):
            output = heapq.heappop(maxHeap)
        return -output