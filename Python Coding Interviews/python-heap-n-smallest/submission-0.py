import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    smallest_element_arr = heapq.nsmallest(1, arr)
    min_element = heapq.heappop(smallest_element_arr)
    return min_element


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    return heapq.nsmallest(4, arr)


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    two_min_elements = heapq.nsmallest(2, arr)
    two_min_elements = list(two_min_elements)
    two_min_elements.sort(reverse=True)
    return two_min_elements


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

