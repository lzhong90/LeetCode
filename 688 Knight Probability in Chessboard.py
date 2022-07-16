class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1
        
        if n < 3:
            return 0
        
        if row >= n or column >= n:
            return 0
        
        
        def neighbours(x,y):
            return [(x-2, y+1), (x-2,y-1), (x+2, y-1), (x+2, y+1), (x-1, y+2), (x+1, y+2), (x-1, y-2), (x+1, y-2)]
        
        def valid(x, y):
            if  0 <= x < n and 0 <= y < n:
                return True
            else:
                return False
            
             
        i = 0
        
        arr = [[0 for i in range(n)] for j in range(n)] 
        arr[row][column] = 1
        
        for i in range(k):
            tmp = [[0 for i in range(n)] for j in range(n)]
            for j in range(n):
                for v in range(n):
                    if arr[j][v] != 0:
                        for a, b in neighbours(j,v):
                            if valid(a,b):
                                tmp[a][b] += arr[j][v]/8
            arr = tmp
        
        res = 0
        
        for i in range(n):
            for j in range(n):
                res += arr[i][j]
            
        return res
