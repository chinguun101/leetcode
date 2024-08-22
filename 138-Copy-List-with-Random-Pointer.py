\\\
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
\\\

class Solution(object):
    def copyRandomList(self, head):
        \\\
        :type head: Node
        :rtype: Node
        \\\
        has={None:None}
        curr=head
        while curr:
            copy=Node(curr.val)
            has[curr]=copy
            curr=curr.next
        curr=head
        while curr:
            copy=has[curr]
            copy.random=has[curr.random]
            copy.next = has[curr.next]
            curr=curr.next
        return has[head]
        