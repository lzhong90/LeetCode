class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1: return 0
        
        
        arr = [[0 for i in range(n)]for j in range(m)]
        
       
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:  
                    arr[0][0] = 1
                    continue
                if obstacleGrid[i][j] == 1:
                    arr[i][j] = 0
                    continue
                if i == 0 and j-1>= 0:
                    arr[i][j] = arr[i][j-1]
                    continue
                if j == 0 and i-1>= 0:
                    arr[i][j] = arr[i-1][j]
                    continue
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
        
            
        return arr[m-1][n-1]
