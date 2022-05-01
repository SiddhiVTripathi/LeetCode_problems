class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        R,C = len(grid1), len(grid1[0])
        cur_count = 0
        
        def dfs(r,c):
            flag = True
            if grid2[r][c]==1:
                grid2[r][c]=-1
                if grid1[r][c]==0:
                    flag=False
                if r-1>=0: flag = dfs(r-1,c) and flag
                if r+1<R: flag =  dfs(r+1,c) and flag 
                if c-1>=0: flag = dfs(r,c-1) and flag 
                if c+1<C: flag = dfs(r,c+1) and flag  
            return flag
        
                    
        for i in range(R):
            for j in range(C):
                if grid2[i][j]==1:
                    if dfs(i,j):
                        cur_count += 1
                    
        return cur_count