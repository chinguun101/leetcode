# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        \\\
        :type head: ListNode
        :rtype: ListNode
        \\\
        curr, reverse=head, None
        while curr:
            temp=curr.next
            curr.next= reverse
            reverse=curr
            curr=temp
            
        return reverse
        