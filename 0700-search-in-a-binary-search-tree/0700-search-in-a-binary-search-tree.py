# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def fun(root,val):
            if root is None:
                return None
            if root.val==val:
                return root
            l=fun(root.left,val)
            r=fun(root.right,val)
            return l if l else r
        return fun(root,val)
                

            
            
