# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #step 1:Find middle
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #Step 2: Reverse second half
        prev=None
        curr=slow

        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode

        #Step 3: Compare both halves
        left=head
        right=prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
        
