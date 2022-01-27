# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {0:[],1:[TreeNode(0)]}
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in Solution.memo:
            ans = []
            for x in range(n):
                y = n-1-x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
                Solution.memo[n] = ans
        return Solution.memo[n]