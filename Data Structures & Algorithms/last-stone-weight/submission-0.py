class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * num for num in stones]
        heapq.heapify(heap)

        while heap:
            if len(heap) == 1:
                return -1 * heap[0]
            largest = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if largest == second:
                continue
            else:
                newWeight = largest - second
                heapq.heappush(heap, newWeight)
        return 0