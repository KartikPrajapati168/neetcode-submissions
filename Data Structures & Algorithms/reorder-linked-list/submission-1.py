# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None

        #Step 1: Find middle
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #Step 2: Split linked list
        second=slow.next
        slow.next=None

        #Step 3: Reverse second half
        prev=None
        curr=second

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        second=prev

        #Step 4:Merge both halves
        first=head

        while second:
            first_next=first.next
            second_next=second.next
            
            first.next=second
            second.next=first_next

            first=first_next
            second=second_next
