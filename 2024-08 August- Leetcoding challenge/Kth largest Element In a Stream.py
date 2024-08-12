import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.minHeap = []
        for num in nums:
            self.heapify(num)

    def add(self, val: int) -> int:
        self.heapify(val)
        return self.minHeap[0]

    def heapify(self, val: int):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
