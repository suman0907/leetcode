# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ptr = ListNode(0,next = head)
        curr= head
        while curr:
            if curr.val==val:
                ptr.next= curr.next
            else:
                ptr= ptr.next
            curr= curr.next        
               
        return dummy.next    


        