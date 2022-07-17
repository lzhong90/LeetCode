class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # everyday there are in total three possible states: hold 0, sold 1, rest 2
        # we need to maximize the value of each possible state on ith day
        # hold[i] = max(hold[i-1], rest[i-1] - price)
        # sold[i] = hold[i-1] + price
        # rest[i] = max(sold[i-1], rest[i-1])
        # 
        
        
        
        l = len(prices)
        hold = [float('-inf')] * (l+1)
        sold = [0]*(l+1)
        rest = [0]*(l+1)
        
        for i in range(1, l+1):
            hold[i] = max(hold[i-1], rest[i-1] -prices[i-1])
            sold[i] = hold[i-1] + prices[i-1]
            rest[i] = max(sold[i-1], rest[i-1])
        
        return max(sold[l], rest[l])
    
    # Space can be optimized
            
