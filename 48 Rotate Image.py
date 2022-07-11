###########################Elegant One############################
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        m = len(matrix)
        for i in range(m):
            for j in range(i+1, m):
                tmp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = tmp
    
    def reflect(self, matrix):
        m = len(matrix)
        for i in range(m):
            matrix[i].reverse()
            
            
 ####################Method 2: Original One#######################
class Solution(object):
  def rotate(self, matrix):
    n = len(matrix)
    
    for i in range(n//2 + n%2):
      for j in range(n//2):
        tmp = matrix[n-1-j][i]
        matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
        matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
        matrix[j][n-1-i] = matrix[i][j]
        matrix[i][j] = tmp
