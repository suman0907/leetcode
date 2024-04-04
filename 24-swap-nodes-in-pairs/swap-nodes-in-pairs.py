# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        dummy = ptr = ListNode() 
        while curr and curr.next:
            odd = curr
            even = curr.next
            curr = curr.next.next
            ptr.next = even
            ptr = ptr.next
            ptr.next= odd
            ptr = ptr.next
            ptr.next = None 
        if curr and not curr.next:
            ptr.next  = curr        
        return dummy.next    
        