class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        R,C = len(grid), len(grid[0])
        cur_count = 0
        
        def dfs(r,c):
            cur_count=0
            if grid[r][c]==1:
                cur_count+=1
                grid[r][c]=-1
                
                if r-1>=0: cur_count+=dfs(r-1,c)
                if r+1<R: cur_count+=dfs(r+1,c)
                if c-1>=0: cur_count+=dfs(r,c-1)
                if c+1<C: cur_count+=dfs(r,c+1)
            return cur_count
        for i in range(R):
            for j in range(C):
                if i==0 or j==0 or i==R-1 or j==C-1:
                    if grid[i][j]==1:
                        dfs(i,j)
                    
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    cur_count += dfs(i,j)
                    
        return cur_count