# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        \\\
        :type root: TreeNode
        :rtype: List[List[int]]
        \\\
        res=[]
        queue=deque()
        if root:
            queue.append(root)
        while len(queue)>0:
            lst=[]
            for i in range(len(queue)):
                curr=queue.popleft()
                lst.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(lst)
        return res