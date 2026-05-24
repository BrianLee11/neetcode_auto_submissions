class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_negative = []
        for number in nums:
            nums_negative.append(-1*number)

        self.heap = nums_negative

        heapq.heapify(self.heap)
        print(self.heap)

        while k > 0:
            max_number_negative = heapq.heappop(self.heap)
            k -= 1
        
        return -1 * max_number_negative


