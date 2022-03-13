class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        
        mask = [[0]*n for _ in range(n)]

        for site in dig:
            mask[site[0]][site[1]]=1
            
        count = 0
        for artifact in artifacts:
            flag = True
            for i in range(artifact[0],artifact[2]+1):
                for j in range(artifact[1],artifact[3]+1):

                    if mask[i][j]==0:
                        flag =False
                        break
                if flag==False:
                    break
            if flag:
                count+=1
        return count   