class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [[0 for i in range(n)] for i in range(m)]
   
        
        arr[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j-1 >= 0:
                    arr[i][j] = arr[i][j-1]
                elif j==0 and i-1 >= 0:
                    arr[i][j] = arr[i-1][j]
                elif i-1 >= 0 and j-1 >= 0:
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
        print(arr)   
        
        return arr[m-1][n-1]
