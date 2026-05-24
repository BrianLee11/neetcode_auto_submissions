class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cumulative_cost = [0] * len(cost)
        cumulative_cost[0] = cost[0]
        cumulative_cost[1] = cost[1]

        for index in range(2, len(cost)):
            cumulative_cost[index] = cost[index] + min(cumulative_cost[index-1], cumulative_cost[index-2])

        return min(cumulative_cost[-1], cumulative_cost[-2])

