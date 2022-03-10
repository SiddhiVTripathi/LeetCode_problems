# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root, val, depth, curDepth):
        if root==None:
            return    
        
        if curDepth==depth-1:
            leftSub = TreeNode(val=val,left=root.left)
            rightSub = TreeNode(val=val,right=root.right)
            root.left,root.right = leftSub,rightSub
            return
        
        self.dfs(root.right,val,depth,curDepth+1)
        self.dfs(root.left,val,depth,curDepth+1)
            
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            
            return TreeNode(val=val,left=root)
        self.dfs(root,val,depth,1)
        return root