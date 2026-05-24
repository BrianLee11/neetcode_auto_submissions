class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index in range(len(stones)):
            stones[index] = -1 * stones[index]

        self.heap = stones


        while len(self.heap) > 1:
            heapq.heapify(self.heap)
            max_value_1 = -1 * heapq.heappop(self.heap)
            max_value_2 = -1 * heapq.heappop(self.heap)

            if max_value_1 != max_value_2:
                value = max_value_1 - max_value_2
                heapq.heappush(self.heap, -1 * value)

        if len(self.heap) == 0:
            return 0
        elif len(self.heap) == 1:
            return self.heap[0] * -1

            