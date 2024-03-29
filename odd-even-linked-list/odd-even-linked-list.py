# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        ref_ptr = None
        if head:
            ref_ptr =even= head.next
        while (odd and odd.next) and (even and even.next):
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        if odd:
            odd.next = ref_ptr
        return head             
        