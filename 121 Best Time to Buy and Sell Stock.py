class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        l = len(prices)
        
        if l <= 1:
            return 0
       
        mx = 0
        mn = prices[0]

        for i in range(l):
            if prices[i] < mn:
                mn = prices[i]
            else:
                mx = max(mx, prices[i] - mn)
        
        return mx
     
############################
