class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i,j)
                    cnt += 1
        return cnt
    
    def dfs(self, grid, i,j):
        
        if i < 0 or j < 0 or j > len(grid[0])-1 or i > len(grid)-1 or grid[i][j] != '1':
            return
        
        grid[i][j] = '*'
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
