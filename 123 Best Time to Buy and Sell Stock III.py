class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # on the ith day, in total four state: first buy, first sell, second buy, second sell
        # buy1[i] = max(buy1[i-1], -price[i])
        # sell1[i] = max(buy1[i-1]+price[i], sell1[i-1])
        # buy2[i] = max(buy2[i-1], sell1[i-1]-price)
        # sell2[i] = max(buy2[i-1]+price[i], sell2[i-1])
        
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        
        for i in prices:
            buy1 = max(buy1, -i)
            sell1 = max(buy1+i, sell1)
            buy2 = max(buy2, sell1-i)
            sell2 = max(buy2+i, sell2)
        return sell2
