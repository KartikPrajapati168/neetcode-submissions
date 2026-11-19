# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import sys

sys.setrecursionlimit(200000)

class Solution:

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        right_head = self.removeNodes(head.next)
        
        head.next=right_head
        
        if right_head is not None and head.val < right_head.val:
            return right_head
        
        return head