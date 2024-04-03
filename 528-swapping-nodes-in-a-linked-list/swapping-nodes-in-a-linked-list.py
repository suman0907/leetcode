# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow= fast = dummy
        while fast and k>0:
            fast = fast.next
            k -=1
        ptr = fast  
        
        while fast:
            fast = fast.next
            slow= slow.next   
        val = ptr.val
        ptr.val =slow.val
        slow.val = val
        return dummy.next

                
        