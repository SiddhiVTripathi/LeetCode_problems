class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)
        grid = [[[0,0] for i in range(l2+1)] for j in range(l2+1)]
        sum=0
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if s[i-1]==t[j-1]:
                    grid[i][j][0]=1+grid[i-1][j-1][0]
                    grid[i][j][1]=grid[i-1][j-1][1]
                else:
                    grid[i][j][1]=1+grid[i-1][j-1][0]
                    
                sum+=grid[i][j][1]
        return sum