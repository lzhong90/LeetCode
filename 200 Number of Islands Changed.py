class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = []
        
        m = len(grid)
        n = len(grid[0])
        
        lands = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' or (i,j) in lands:
                    continue
                island = set()
                if self.isBorder(i,j,m,n):
                    island.add('*')
                lands.add((i,j))
                island.add((i,j))
                stck = [(i,j)]
                while len(stck) > 0:
                    idxi,idxj = stck.pop()
                    a = self.validNeighIndice(idxi, idxj,m,n)
                    for x in a:
                        if x not in island and grid[x[0]][x[1]] == '1':
                            stck.append(x)
                            island.add(x)
                            lands.add(x)
                            if self.isBorder(x[0],x[1],m,n):
                                island.add('*')
                res.append(island)
                #print(lands)
        rmv = []
        for i in res:
            if '*' not in i:
                rmv.append(list(i))
               
        return rmv
                
                    
                    
                    
                    
                    
    def isValidIndex(self, i, j,m,n):
        if i >= 0 and j >= 0 and i < m and j < n:
            return True
        else:
            return False
    def validNeighIndice(self, i, j,m,n):
        l = []
        if self.isValidIndex(i-1,j,m,n):
            l.append((i-1,j))
        if self.isValidIndex(i+1,j,m,n):
            l.append((i+1,j))
        if self.isValidIndex(i,j-1,m,n):
            l.append((i,j-1))
        if self.isValidIndex(i,j+1,m,n):
            l.append((i,j+1))
        
        return l
    
    def isBorder(self,i,j,m,n):
        if i == 0 or j == 0 or j==n-1 or i == m-1:
            return True
        else:
            return False
