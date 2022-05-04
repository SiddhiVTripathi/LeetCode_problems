class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    queue.append((1,i,j))
                    
        res = -1
        while queue:
            w,i,j = queue.pop(0)
            for di,dj in [(0,-1),(0,1),(1,0),(-1,0)]:
                new_i,new_j = i+di,j+dj
                
                if 0<=new_i<m and 0<=new_j<n:
                    if grid[new_i][new_j]==0:
                        grid[new_i][new_j]=w
                        queue.append((w+1,new_i,new_j))
                        res = max(res,w)
                        
        return res