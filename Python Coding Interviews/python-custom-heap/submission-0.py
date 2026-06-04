import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    reverse_arr = []

    for num in nums:
        heapq.heappush(heap, num)
    
    while heap:
        element = heapq.heappop(heap)
        reverse_arr.append(element)

    reverse_arr = reverse_arr[::-1]

    return reverse_arr

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
