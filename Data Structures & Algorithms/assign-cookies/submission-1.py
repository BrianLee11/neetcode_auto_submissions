from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        demand = g
        supply = s

        demand.sort()
        supply.sort()

        index_demand = 0
        index_supply = 0

        length_demand = len(demand)
        length_supply = len(supply)

        int_number_success = 0

        while index_demand < length_demand and index_supply < length_supply:
            if demand[index_demand] <= supply[index_supply]:
                int_number_success += 1
                index_demand += 1
                index_supply += 1
            else:
                index_supply += 1

        return int_number_success
