class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[1])
        
        sum =0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==1 and not (i==0 or j==0):
                    matrix[i][j]=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])+1
                
                sum+=matrix[i][j]
                    
        print(matrix)
        return sum