class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []

        for point in points:
            distance = (point[0]**2) + (point[1]**2)

            heapq.heappush(minHeap, (distance, point))

        output = []
        for _ in range(k):
            output.append(heapq.heappop(minHeap)[1])
        




        return output
            





