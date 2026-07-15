# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        r=[]
        def fun(root):
            if root==None:
                return
            fun(root.left)
            r.append(root.val)
            fun(root.right)
        fun(root)
        m=float('inf')
        for i in range(len(r)-1):
            m=min(m,abs(r[i]-r[i+1]))
        return m

        