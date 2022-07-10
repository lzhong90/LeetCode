class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        opt = [0]*l
        opt[0] = 0
        opt[1] = 0
        for i in range(2, l):
            opt[i] = min(opt[i-1]+cost[i-1], cost[i-2]+ opt[i-2])
        
        return min(opt[l-1]+cost[l-1], opt[l-2]+cost[l-2])
    
