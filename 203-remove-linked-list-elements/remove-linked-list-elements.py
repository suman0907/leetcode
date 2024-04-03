# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ptr = ListNode()
        curr = head
        while curr:
            if curr.val!=val:
                ptr.next = curr
                ptr = ptr.next
                curr = curr.next
                ptr.next = None
            else:
                curr = curr.next
        return dummy.next           
        