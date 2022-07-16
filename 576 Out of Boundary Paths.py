class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if m < 1 or n < 1:
            return 0
        
        if maxMove < 1:
            return 0
        
        def neighbours(x,y):
            return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
        def valid(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return False
            else:
                return True
        
        modulo = 10**9+7
        arr = [[0 for v in range(n)] for j in range(m)] 
        
        print(len(arr))
        
        for i in range(1, maxMove+1):
            tmp = [[0 for v in range(n)] for j in range(m)] 
            for j in range(m):
                for k in range(n):
                    for a, b in neighbours(j ,k):
                        if not valid(a, b):
                            tmp[j][k] += 1
                        else:
                            tmp[j][k] += arr[a][b]
            arr = tmp
        
        return arr[startRow][startColumn]%modulo
