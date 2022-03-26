class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda k: (k[0]-k[1]))
        fh = sum(cost[0] for cost in costs[:len(costs)//2])
        sh = sum(cost[1] for cost in costs[len(costs)//2:])
        return fh+sh