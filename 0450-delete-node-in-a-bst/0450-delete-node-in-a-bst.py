# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getmin(r):
            if r is None:
                return None
            while(r.left):
                r=r.left
            return r
        def fun(root,key):
            if root==None:
                return None
            if key<root.val:
                root.left=fun(root.left, key)
            if key>root.val:
                root.right=fun(root.right, key)
            if key==root.val:
                if root.left is None and root.right is None:
                    return None
                if root.left is not None and root.right is None:
                    return root.left
                if root.left is  None and root.right is not None:
                    return root.right
                else:
                    temp=getmin(root.right)
                    root.val=temp.val
                    root.right=fun(root.right,temp.val)
            return root

        return fun(root, key)

             
            
        