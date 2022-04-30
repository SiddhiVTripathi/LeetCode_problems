class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        R,C = len(grid), len(grid[0])
        max_count = 0
        
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
                if grid[i][j]==1:
                    cur_count = dfs(i,j)
                    max_count = max(max_count,cur_count)
                    
        return max_count