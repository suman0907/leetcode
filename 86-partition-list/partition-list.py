# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ptr1 = ListNode()
        right = ptr2=  ListNode()
        curr = head 
        while curr:
            if curr.val<x:
                ptr1.next = ListNode(curr.val)
                ptr1 = ptr1.next
            else:
                ptr2.next = ListNode(curr.val)
                ptr2 = ptr2.next
            curr = curr.next    
        ptr1.next = right.next
        return left.next        

        