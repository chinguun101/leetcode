# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        \\\
        :type lists: List[ListNode]
        :rtype: ListNode
        \\\
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]


    def mergeList(self,l1,l2):
        node=dummy=ListNode()
        while l1 and l2:
            if l1.val<l2.val:
                node.next=l1
                l1=l1.next
            else:
                node.next=l2
                l2=l2.next
            node=node.next
            
        node.next=l1 or l2
        return dummy.next