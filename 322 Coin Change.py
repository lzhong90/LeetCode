#BFS
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc =  0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1
      
  ###############
  # DP
  class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        l = len(coins)
        if l < 1:
            return  -1
        
        arr = [float(inf) for i in range(amount+1)]
        arr[0] = 0
        

        
        #print(min(arr[:][0]))
        
        
        for i in range(1, amount+1):
            mn = float('inf')
            for j in range(l):
                if coins[j] == i:
                    mn = 1
                elif coins[j] < i:
                    mn = min(mn, arr[i-coins[j]]+1)
            arr[i] = mn

        return arr[amount] if arr[amount] != float('inf') else -1
