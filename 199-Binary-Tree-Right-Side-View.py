# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        \\\
        :type root: TreeNode
        :rtype: List[int]
        \\\
        queue=deque()
        res=[]
        if root:
            queue.append(root)
            res.append(root.val)
        while len(queue)>0:
            for i in range(len(queue)):
                curr=queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if queue:
                res.append(queue[-1].val)  
        return res