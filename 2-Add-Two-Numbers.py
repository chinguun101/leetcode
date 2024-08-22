# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry=0
        dummy=cur=ListNode()
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            value=val1+val2+carry
            carry= value//10
            value=value%10

            cur.next=ListNode(value)

            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
        
        
        \\\
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        \\\
        