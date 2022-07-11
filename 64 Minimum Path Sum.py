class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        if m == 1 and n == 1:
            return grid[0][0]
        
        if m<1 or n<1:
            raise ValueError('xxx')
            
        
        arr = [[0 for i in range(n)]for i in range(m)]
        
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j==0:
                    arr[0][0] = grid[0][0]
                    continue
                if i== 0 and j-1 >= 0:
                    arr[i][j] = arr[i][j-1] + grid[i][j]
                    continue
                if j == 0 and i-1 >= 0:
                    arr[i][j] = arr[i-1][j] + grid[i][j]
                    continue
                arr[i][j] = min(arr[i-1][j], arr[i][j-1]) + grid[i][j]
        return arr[m-1][n-1]
