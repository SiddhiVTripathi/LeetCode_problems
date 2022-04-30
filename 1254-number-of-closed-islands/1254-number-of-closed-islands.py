class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        R,C = len(grid),len(grid[0])
        ans =0
        def dfs(r,c):
            if grid[r][c]==0:
                grid[r][c]=-1
                if r-1>=0: dfs(r-1,c)
                if r+1<R: dfs(r+1,c)
                if c-1>=0: dfs(r,c-1)
                if c+1<C: dfs(r,c+1)
        
        for i in range(R):
            for j in range(C):
                if j==0 or j==C-1 or i==0 or i==R-1:
                    if grid[i][j]==0:
                        dfs(i,j)
        print(grid)                
        for i in range(R):
            for j in range(C):
                if grid[i][j]==0:
                    ans+=1
                    dfs(i,j)
        return ans