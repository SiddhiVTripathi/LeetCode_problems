class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        seen=set()
        dp=[[-1 for i in range(0,n)] for j in range(0,n)]
        index=0
        for x1,y1,x2,y2 in artifacts:
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    dp[i][j]=index
            index+=1
        ans=set()
        for i,j in dig:
            dp[i][j]=-1
        for i in range(0,n):
            for j in range(0,n):
                if dp[i][j]!=-1 and dp[i][j] not in ans:
                    ans.add(dp[i][j])
        return len(artifacts)-len(ans)