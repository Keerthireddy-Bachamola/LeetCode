# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        s=0
        def fun(root,p,gp):
            nonlocal s
            if root is None:
                return
            if gp is not None and gp.val%2==0:
                s+=root.val
            fun(root.left,root,p)
            fun(root.right,root,p)
        fun(root,None,None)
        return s
        