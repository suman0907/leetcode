# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = next_p = head
        prev = None
        while curr is not None:
            next_p = curr.next
            curr.next = prev
            prev = curr 
            curr = next_p
        return prev    
        