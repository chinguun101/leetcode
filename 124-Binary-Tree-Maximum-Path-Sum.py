# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        \\\
        :type root: TreeNode
        :rtype: int
        \\\
        res=[root.val]
        def dfs(root):
            if not root:
                return 0
            left,right=dfs(root.left), dfs(root.right)
            left,right=max(left,0), max(right,0)
            res[0]=max(res[0],root.val+left+right)
            return root.val+max(left,right)
        dfs(root)
        return res[0]
        